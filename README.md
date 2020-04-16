# Turkish Treebanks

![](https://github.com/google-research-datasets/turkish-treebanks/workflows/Build%20Status/badge.svg)

A human-annotated morphosyntactic treebank for Turkish.

This is not an official Google product.

## Dataset Metadata

<div itemscope itemtype="http://schema.org/Dataset">
  <table>
    <tr>
      <td>name</td>
      <td><code itemprop="name">Turkish Web Treebank</code></td>
    </tr>
    <tr>
      <td>description</td>
      <td><code itemprop="description">A human-annotated morphosyntactic
      treebank for Turkish.</code></td>
    </tr>
    <tr>
      <td>sameAs</td>
      <td><code itemprop="sameAs">https://github.com/google-research-datasets/turkish-treebanks</code></td>
    </tr>
    <tr>
      <td>license</td>
      <td><code itemprop="license">http://www.apache.org/licenses/LICENSE-2.0.txt</code></td>
    </tr>
  </table>
</div>

## Dataset Description

Turkish Web Treebank (TWT) consists of 4,851 sentences (66,466 words, and
81,370 inflectional group tokenized tokens), which are manually annotated for
segmentation, morphology, part-of-speech and dependency relations. It is
composed of two sections: [web][3] and [Wikipedia][4]. Web section is built by
sampling and annotating 2,541 sentences from a representative set of Turkish
Forum, Blog, How-to, Review & Guides webpages. Wikipedia section is built by
sampling a sentence from 2,310 Turkish Wikipedia pages and annotating them.

|           | Sentences | Words  | Tokens |
|:--------  |:--------- |:------ |:------ |
| Web       | 2,541     | 26,519 | 32,422 |
| Wiki      | 2,310     | 39,947 | 48,498 |

In terms of splits, in our experiments, we use every 9th sentence in above
linked CoNLL-U format files as the development set, and every 10th sentence as
the test set. All other sentences belong to the training set. We advise you to
do the same for comparable results. [Python API][11] section describes the
library that you can use to retrieve the splits.

### Data format

Both sections of TWT is provided in CoNLL-U format in separate files. We follow
the descriptions for the fields of the CoNLL-U format as they are defined in the
[documentation of the Universal Dependencies project][6], only with the
following differences:

* we use the original **UPOS** field to specifiy the coarse part-of-speech
  of the tokens.
* we use the original **XPOS** field to specify the fine part-of-speech
  of the tokens.
* we do not use the **DEPS** field as we do not provide enhanced dependency
  graph annotations, therefore we use "\_" to mark the value of this field
  for all tokens.
* since our tokens correspond to inflectional groups, we only list the
  lemmas for multi inflectional group words in the **LEMMA** field of the first
  inflectional group; we mark the **LEMMA** field of all other inflectional
  groups of such words with "\_".

Below is an example annotation for the sentence "*Üst öğrenimi bitirmenin
sağladığı haklar...*" in CoNNL-U format as we use it.

| **ID** | **FORM** | **LEMMA** | **CPOS** | **FPOS** | **FEATS**                                                                   | **HEAD** | **DEPREL** | **DEPS** | **MISC**      |
|:------ |:-------- |:--------- |:-------- |:-------- |:--------------------------------------------------------------------------- |:-------- |:---------- |:-------- |:------------- |
| 1      | Üst      | üst       | ADJ      | JJ       | Proper=False                                                                | 2        | amod       | _        | _             |
| 2      | öğrenimi | öğrenim   | NOUN     | NN       | PersonNumber=A3sg\|Possessive=Pnon\|Case=Acc\|Proper=False                  | 4        | dobj       | _        | _             |
| 3      | bit      | bit       | VERB     | VB       | Proper=False                                                                | 4        | ig         | _        | SpaceAfter=No |
| 4      | ir       | _         | VERB     | VB       | Derivation=Cau\|Polarity=Pos\|Proper=False                                  | 5        | ig         | _        | SpaceAfter=No |
| 5      | menin    | _         | NOUN     | VN       | Derivation=Nonf\|PersonNumber=A3sg\|Possessive=Pnon\|Case=Gen\|Proper=False | 7        | poss       | _        | _             |
| 6      | sağla    | sağla     | VERB     | VB       | Polarity=Pos\|Proper=False                                                  | 7        | ig         | _        | SpaceAfter=No |
| 7      | dığı     | _         | ADJ      | VJ       | Derivation=PastPart\|Possessive=P3sg\|Proper=False                          | 8        | rcmod      | _        | _             |
| 8      | haklar   | hak       | NOUN     | NN       | PersonNumber=A3sg\|Possessive=Pnon\|Case=Bare\|Proper=False                 | 0        | root       | _        | SpaceAfter=No |
| 9      | ...      | ...       | PUNCT    | .        | Proper=False                                                                | 8        | p          | _        | _             |

### Annotations

Part-of-speech and morphology layer of TWT is annotated using the
[Tukish morphological analyzer][7]. You can see that repository for the full
part-of-speech and morphological feature category-value tagsets and their
descriptions.

The dependency layer is annotated using a label set of 44 dependency relations.
Below table provides the descriptions for the dependency relations that are
used in annotating the TWT.

| Label      | Description                                                  |
|:---------- |:------------------------------------------------------------ |
| ROOT       | root of the sentence                                         |
| acomp      | adjectival complement                                        |
| advcl      | adverbial clause                                             |
| advmod     | adverbial modifier                                           |
| amod       | adjectival modifier of NP                                    |
| appos      | appositional modifier of NP                                  |
| attr       | attribute dependent of a copular verb                        |
| aux        | auxiliary verb                                               |
| cc         | coordinating conjunction                                     |
| ccomp      | clausal complement of a verb or adjective                    |
| clas       | classifier                                                   |
| conj       | conjunct                                                     |
| csubj      | clausal subject                                              |
| det        | determiner                                                   |
| discourse  | interjections and other discourse elements                   |
| dislocated | dislocated elements                                          |
| dobj       | direct object                                                |
| goeswith   | parts of a word that were mistokenized                       |
| ig         | inflectional group                                           |
| iobj       | indirect object                                              |
| list       | list for chains of comparable items                          |
| mark       | complementizer (words introducing finite subordinate clause) |
| mwe        | multiword expression                                         |
| narg       | argument of a nominal                                        |
| neg        | negation                                                     |
| nn         | nominal modifier                                             |
| npadvmod   | noun phrase used as an adverbial modifier of a verb          |
| nsubj      | nominal subject                                              |
| num        | numeric modifier of a noun                                   |
| number     | element of compound number                                   |
| p          | punctuation                                                  |
| parataxis  | parataxis                                                    |
| pcomp      | clausal complement of postposition                           |
| pobj       | object of postposition                                       |
| poss       | possessive modifier                                          |
| preconj    | preconjuct                                                   |
| predet     | predeterminer                                                |
| prep       | postposition                                                 |
| prt        | particle                                                     |
| rcmod      | relative clause modifier                                     |
| remnant    | ellipsis                                                     |
| tmod       | temporal modifier                                            |
| vocative   | vocative                                                     |
| xcomp      | open clausal complement                                      |

Following the Universal Dependencies annotation scheme, we also provide shallow
segmentation annotations as miscellaneous features on tokens which are not
whitespace segmented from the following ones in source text. We mark them with
"SpaceAfter=No" feature category-value pair.

## Python API

Together with the dataset we also provide a [Python API][5] that can be used to
read annotated sentences (per web or Wikipedia sections and/or "train", "dev",
"test" splits).

If you are using [Bazel][8], you can depend on this repository as an external
dependency of your project by adding the following to your WORKSPACE file:

```
git_repository(
  name = "google_research_turkish_treebanks",
  remote = "https://github.com/google-research-datasets/turkish-treebanks.git",
  tag = "{version-tag}",
)
```

Then, you can simply use
`@google_research_turkish_treebanks//turkish_treebanks:read` as a
dependecy of your relevant `py_library` or `py_binary` BUILD targets.

The API is also available on PyPi. To install the latest release from PyPi, run:

```
python3 -m pip install turkish-treebanks
```

To install from source, run below from the project root directory (preferably
within a Python virtual environment):

```
bazel build //...
bazel-bin/setup install
```

## Requirements

To build and run the tools install [Bazel version 3.0.0][9],
[Python 3.7.5 (or a newer version)][10]. All other intrinsic dependencies will
be imported, built and taken care of by Bazel according to the [WORKSPACE][2]
setup. If you are installing from PyPi, you need [pip][12].

## Citing

If you use or discuss this dataset in your work, please cite:

Kayadelen, T., Öztürel, A. & Bohnet, B. (2020). A Gold Standard Dependency
Treebank for Turkish. In *Proceedings of the 12th Language Resources and
Evaluation Conference (LREC 2020)*.

```
@inproceedings{
  title = "A Gold Standard Dependency Treebank for Turkish",
  author = "Kayadelen, Tolga and \"{O}zt\"{u}rel, Adnan and Bohnet, Bernd"
  booktitle = "Proceedings of the 12th Language Resources and Evaluation
      Conference (LREC 2020)",
  year = "2020",
}
```

## Contact

If you have a technical question regarding the dataset, code or publication,
please create an issue in this repository.

## License

Unless otherwise noted, all original files are licensed under
[Apache License Version 2.0][1].

[1]: ./LICENSE
[2]: ./WORKSPACE
[3]: ./data/web.conllu
[4]: ./data/wiki.conllu
[5]: ./turkish_treebanks/read.py
[6]: https://universaldependencies.org/format.html
[7]: https://github.com/google-research/turkish-morphology
[8]: https://bazel.build/
[9]: https://docs.bazel.build/versions/master/install.html
[10]: https://www.python.org/downloads/
[11]: #python-api
[12]: https://pip.pypa.io/en/stable/installing/
