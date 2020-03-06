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

"""Tests for lib.read."""

from lib import read

from absl.testing import absltest
from absl.testing import parameterized


class SentencesTest(parameterized.TestCase):

  @parameterized.named_parameters([
      {
          "testcase_name": "Unfiltered",
          "section": None,
          "split": None,
          "expected_sentence_count": 4851,
          "expected_token_count": 81370,
          "expected_first_sentence_id": "tr-forum:00000222:S023",
          "expected_first_sentence_text": "Burda da öylemi yoksa kiloyla mı ?",
      },
      {
          "testcase_name": "TrainSplit",
          "section": None,
          "split": "train",
          "expected_sentence_count": 3881,
          "expected_token_count": 64707,
          "expected_first_sentence_id": "tr-forum:00000222:S023",
          "expected_first_sentence_text": "Burda da öylemi yoksa kiloyla mı ?",
      },
      {
          "testcase_name":
              "DevSplit",
          "section":
              None,
          "split":
              "dev",
          "expected_sentence_count":
              485,
          "expected_token_count":
              8638,
          "expected_first_sentence_id":
              "tr-review:00000378:S021",
          "expected_first_sentence_text":
              ("Günde 1-2 öğün, protein bakımından zengin yiyecekler yemek bu"
               " miktarlarda protein almanızı sağlayacaktır."),
      },
      {
          "testcase_name":
              "TestSplit",
          "section":
              None,
          "split":
              "test",
          "expected_sentence_count":
              485,
          "expected_token_count":
              8025,
          "expected_first_sentence_id":
              "tr-forum:00001366:S004",
          "expected_first_sentence_text":
              ("Bu konuda sizlerle genel işletim sistemi yönetimi ve"
               " iyileştirmeleri hakkında birkaç bilgi ileteceğim."),
      },
      {
          "testcase_name": "Web",
          "section": "web",
          "split": None,
          "expected_sentence_count": 2541,
          "expected_token_count": 32422,
          "expected_first_sentence_id": "tr-forum:00000222:S023",
          "expected_first_sentence_text": "Burda da öylemi yoksa kiloyla mı ?",
      },
      {
          "testcase_name": "WebTrainSplit",
          "section": "web",
          "split": "train",
          "expected_sentence_count": 2033,
          "expected_token_count": 25906,
          "expected_first_sentence_id": "tr-forum:00000222:S023",
          "expected_first_sentence_text": "Burda da öylemi yoksa kiloyla mı ?",
      },
      {
          "testcase_name":
              "WebDevSplit",
          "section":
              "web",
          "split":
              "dev",
          "expected_sentence_count":
              254,
          "expected_token_count":
              3260,
          "expected_first_sentence_id":
              "tr-review:00000378:S021",
          "expected_first_sentence_text":
              ("Günde 1-2 öğün, protein bakımından zengin yiyecekler yemek bu"
               " miktarlarda protein almanızı sağlayacaktır."),
      },
      {
          "testcase_name":
              "WebTestSplit",
          "section":
              "web",
          "split":
              "test",
          "expected_sentence_count":
              254,
          "expected_token_count":
              3256,
          "expected_first_sentence_id":
              "tr-forum:00001366:S004",
          "expected_first_sentence_text":
              ("Bu konuda sizlerle genel işletim sistemi yönetimi ve"
               " iyileştirmeleri hakkında birkaç bilgi ileteceğim."),
      },
      {
          "testcase_name":
              "Wiki",
          "section":
              "wiki",
          "split":
              None,
          "expected_sentence_count":
              2310,
          "expected_token_count":
              48948,
          "expected_first_sentence_id":
              ("http://tr.wikipedia.org/wiki/Christian_(g%C3%BCre%C5%9F%C3%A7i)"
               ":S057"),
          "expected_first_sentence_text":
              ("Kemerlerini Aralık ayında ki Armageddon'da dört takımın"
               " katıldığı eliminasyon maçında Booker T ve Goldust'a"
               " kaybettiler."),
      },
      {
          "testcase_name":
              "WikiTrainSplit",
          "section":
              "wiki",
          "split":
              "train",
          "expected_sentence_count":
              1848,
          "expected_token_count":
              38801,
          "expected_first_sentence_id":
              ("http://tr.wikipedia.org/wiki/Christian_(g%C3%BCre%C5%9F%C3%A7i)"
               ":S057"),
          "expected_first_sentence_text":
              ("Kemerlerini Aralık ayında ki Armageddon'da dört takımın"
               " katıldığı eliminasyon maçında Booker T ve Goldust'a"
               " kaybettiler."),
      },
      {
          "testcase_name":
              "WikiDevSplit",
          "section":
              "wiki",
          "split":
              "dev",
          "expected_sentence_count":
              231,
          "expected_token_count":
              5378,
          "expected_first_sentence_id":
              "http://tr.wikipedia.org/wiki/B%C3%BCy%C3%BCk_say%C4%B1lar:S022",
          "expected_first_sentence_text":
              ("Gözlemlenebilir evren 93 milyar ışık yılı, (8,8 × 10 metre)"
               " genişliğindedir ve yaklaşık 125 milyar (1,25 × 10) galaksi"
               " içindeki 5 × 10 yıldızdan oluşur."),
      },
      {
          "testcase_name":
              "WikiTestSplit",
          "section":
              "wiki",
          "split":
              "test",
          "expected_sentence_count":
              231,
          "expected_token_count":
              4769,
          "expected_first_sentence_id":
              "http://tr.wikipedia.org/wiki/%C5%9Eebe%C5%9F_Muharebesi:S033",
          "expected_first_sentence_text":
              ("Lazarethane'de Sadrâzam Koca Yûsuf Paşa başkanlığında yapılan"
               " ordu müzakerelerinde kış mevsimi ciddiyetle başlamadan ve"
               " Avusturya ordusunun Muhaddiye Muharebesi yenilgisinden kendini"
               " toparlamasına imkan sağlamadan, hemen harekata başlanmasına ve"
               " bu nedenle Şebeş Boğazı'nda tahkimli mevzilere girmiş olan"
               " Avusturya ordusu üzerine gidilmesine karar verildi."),
      },
  ])
  def test_reads_sentences(self, section, split, expected_sentence_count,
                           expected_token_count, expected_first_sentence_id,
                           expected_first_sentence_text):
    sentences = tuple(read.sentences(section, split))
    actual_sentence_count = len(sentences)
    self.assertEqual(expected_sentence_count, actual_sentence_count)
    actual_token_count = sum(len(s.token) for s in sentences)
    self.assertEqual(expected_token_count, actual_token_count)
    actual_first_sentence_id = sentences[0].id_
    self.assertEqual(expected_first_sentence_id, actual_first_sentence_id)
    actual_first_sentence_text = sentences[0].text
    self.assertEqual(expected_first_sentence_text, actual_first_sentence_text)

  def test_reads_tokens(self):
    sentences = tuple(read.sentences())
    expected_token = read.Token(
        id_=1,
        form="Açık",
        lemma="açık",
        coarse_tag="NOUN",
        fine_tag="NN",
        features=(
            read.Feature(name="PersonNumber", value="A3sg"),
            read.Feature(name="Possessive", value="Pnon"),
            read.Feature(name="Case", value="Bare"),
            read.Feature(name="Proper", value="False"),
        ),
        head=2,
        dependency_relation="ig",
        miscellaneous_features=(read.Feature(name="SpaceAfter", value="No"),),
    )
    actual_token = sentences[1].token[0]
    self.assertEqual(expected_token, actual_token)

  @parameterized.named_parameters([
      {
          "testcase_name": "InvalidSection",
          "section": "foo",
          "split": None,
          "exception": ValueError,
          "error": "Invalid section name 'foo'.",
      },
      {
          "testcase_name": "InvalidSplit",
          "section": None,
          "split": "foo",
          "exception": ValueError,
          "error": "Invalid split specifier 'foo'.",
      },
  ])
  def test_raises_exception(self, section, split, exception, error):
    with self.assertRaisesRegexp(exception, error):
      tuple(read.sentences(section, split))


if __name__ == "__main__":
  absltest.main()
