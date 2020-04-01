# coding=utf-8
# Copyright 2020 The Google Research Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Functions to read Turkish Web Treebank sentence annotations."""

import os
import pathlib
from typing import Generator, Iterable, List, Optional

from turkish_treebanks import twt_pb2

_Feature = twt_pb2.Feature
_Sentence = twt_pb2.Sentence
_Tag = twt_pb2.Tag
_Token = twt_pb2.Token

_ROOT_DIR = pathlib.Path(__file__).parent.parent
_DATA_DIR = os.path.join(_ROOT_DIR, "data")
_PATHS_BY_SECTION = {
    "web": os.path.join(_DATA_DIR, "web.conllu"),
    "wiki": os.path.join(_DATA_DIR, "wiki.conllu"),
}
_VALID_SPLIT_NAMES = [
    "train",
    "dev",
    "test",
]


def _whitespace_trimmed(string: str) -> str:
  """Strips any leading and trailing whitespace off from the string"""
  return string.lstrip().rstrip()


def _split_into_sentences(conll: str) -> List[str]:
  """Tokenizes contents of a CoNLL-U format file by sentence annotations."""
  return [_whitespace_trimmed(s) for s in conll.split("\n\n")]


def _split_into_lines(sentence: str) -> List[str]:
  """Tokenizes CoNLL-U format sentence annotation into lines."""
  return [_whitespace_trimmed(l) for l in sentence.split("\n")]


def _reconstruct_conll_from(sentences: Iterable[str]) -> str:
  """Reconstructs CoNLL-U format file content from sentence annotations."""
  return "\n\n".join(sentences)


def _read_sentences_from(path: str) -> Generator[str, None, None]:
  """Reads and yields sentences of a CoNLL-U format treebank file from the path.

  Args:
    path: path to a CoNLL-U format treebank file from which sentences will be
        read.

  Yields:
    Individual sentence annotations of a CoNLL-U format treebank file.
  """
  with open(path, "r", encoding="utf-8") as reader:
    yield from _split_into_sentences(reader.read())


def _sentence_is_in_split(sentence_index: int, split: str) -> bool:
  """Checks if sentence with given positional index is in the split.

  In order to deterministically sample train/dev/test sentences, this function
  assumes every 9th sentence of a treebank file belongs to the development
  set, and every 10th sentence of a treebank file belongs to the test set. All
  other sentences belong to the training set.

  Args:
    sentence_index: sequential index of the sentence in the source CoNLL-U
        format treebank file (assuming first sentence has index 0).
    split: treebank split (could be 'train', 'test', 'dev').

  Returns:
    True if sentence with given positional index belongs to the specified split.
    Otherwise, returns False.
  """
  if split == "train":
    return sentence_index % 10 < 8
  elif split == "dev":
    return sentence_index % 10 == 8
  elif split == "test":
    return sentence_index % 10 == 9
  else:
    return True


def _validate_sentence(sentence: str) -> None:
  """Checks if a CoNLL-U format sentence annotation is structurally wellformed.

  Args:
    sentence: a CoNNL-U format sentence annotation.

  Raises:
    ValueError: CoNNL-U format sentence annotation is illformed. It is either
        missing sentence id or text annotation, or one of the lines that ought
        to contain token annotations is structurally illformed.
  """
  lines = _split_into_lines(sentence)

  if len(lines) <= 2:
    raise ValueError(
        f"Expecting a sentence to be at least 3 lines in CoNLL-U format,"
        f" but found a {len(sentence)} line sentence annotation:\n{sentence}")

  if not lines[0].startswith("# sent_id = "):
    raise ValueError(
        f"First line of the CoNNL-U format sentence annotation does not have a"
        f" valid sentence id annotation:\n{sentence}")

  if not lines[1].startswith("# text = "):
    raise ValueError(
        f"Second line of the CoNNL-U format sentence annotation does not have a"
        f" valid sentence text annotation:\n{sentence}")

  def _validate_token_line(line: str) -> None:
    if len(line.split("\t")) != 10:
      raise ValueError(f"Illformed CoNNL-U format token annotation:\n{line}")

  for line in lines[3:]:
    _validate_token_line(line)


def _decompose_sentence(sentence: str) -> _Sentence:
  """Parses CoNLL-U format sentence annotation in a sentence protobuf.

  Args:
    sentence: a CoNNL-U format sentence annotation.

  Returns:
    Sentence protobuf that contains annotations for a sentence that is parsed
    from CoNLL-U format sentence annotation.
  """

  def _decompose_comment(line: str, prefix: str) -> None:
    """Decomposes a comment line of CoNNL-U format."""
    return line[len(prefix):]

  def _decompose_features(raw_features: str) -> Generator[_Feature, None, None]:
    """Parses CoNLL-U format features annotations into Feature objects."""
    category_value = (f.split("=") for f in raw_features.split("|") if f != "_")
    yield from (_Feature(category=n, value=v) for n, v in category_value)

  def _decompose_token(line: str) -> _Token:
    """Parses CoNLL-U format token annotations into Token objects."""
    column = line.split("\t")
    return _Token(
        form=column[1],
        lemma=column[2],
        tag=_Tag(coarse=column[3], fine=column[4]),
        feature=_decompose_features(column[5]),
        head=int(column[6]),
        dependency_relation=column[7],
        misc_feature=_decompose_features(column[9]),
    )

  lines = _split_into_lines(sentence)
  return _Sentence(
      sentence_id=_decompose_comment(lines[0], "# sent_id = "),
      text=_decompose_comment(lines[1], "# text = "),
      token=tuple(_decompose_token(l) for l in lines[2:]),
  )


def as_conllu(section: Optional[str] = None,
              split: Optional[str] = None) -> str:
  """Reads sentence annotations of Turkish Web Treebank in CoNLL-U format.

  Args:
    section: optional, section of Turkish Web Treebank whose sentence
        annotations will be read (could be either 'web' or 'wiki'). If
        unspecified sentence annotations from web and Wikipedia sections will
        be read.
    split: optional, treebank split whose sentence annotations will be read
        (could be 'train', 'test', 'dev'). If unspecified sentence annotations
        from all three splits will be read.

  Raises:
    ValueError: invalid section name or split specifier, or source treebank
        files from which the sentence annotations are read is not valid with
        respect to the CoNLL-U format.

  Returns:
    Sentence annotations for the specified treebank and split in CoNNL-U
    treebank file format.
  """
  if section and section not in _PATHS_BY_SECTION:
    raise ValueError(f"Invalid section name '{section}'."
                     f" It can only be one of: 'web', 'wiki'.")

  if split and split not in _VALID_SPLIT_NAMES:
    raise ValueError(f"Invalid split specifier '{split}'."
                     f" It can only be one of: 'train', 'dev', 'test'")

  if section:
    paths = (p for s, p in _PATHS_BY_SECTION.items() if s == section)
  else:
    paths = _PATHS_BY_SECTION.values()

  def _filtered_sentences() -> Generator[str, None, None]:
    for path in sorted(paths):
      for index, sentence in enumerate(_read_sentences_from(path)):
        if _sentence_is_in_split(index, split):
          _validate_sentence(sentence)
          yield sentence

  return _reconstruct_conll_from(_filtered_sentences())


def sentences(section: Optional[str] = None,
              split: Optional[str] = None) -> Generator[_Sentence, None, None]:
  """Reads and yields sentences of Turkish Web Treebank as sentence protobufs.

  Args:
    section: optional, section of Turkish Web Treebank whose sentence
        annotations will be read (could be either 'web' or 'wiki'). If
        unspecified sentence annotations from both web and Wikipedia sections
        will be read.
    split: optional, treebank split whose sentence annotations will be read
        (could be 'train', 'test', 'dev'). If unspecified sentence annotations
        from all three splits will be read.

  Raises:
    ValueError: invalid section name or split specifier, or source treebank
        files from which the sentence annotations are read is not valid with
        respect to the CoNLL-U format.

  Yields:
    Sentence protobufs which contain annotations for the specified treebank
    section and split.
  """
  for sentence in _split_into_sentences(as_conllu(section, split)):
    yield _decompose_sentence(sentence)
