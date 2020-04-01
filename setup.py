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

import setuptools

setuptools.setup(
    name="turkish-treebanks",
    version="1.0.0",
    description="Turkish Web Treebank",
    long_description=("A Python API to read annotations of the Turkish Web"
                      " Treebank (TWT)."),
    url="https://github.com/google-research-datasets/turkish-treebanks",
    download_url=("https://github.com/google-research-datasets/"
                  "turkish-treebanks/releases"),
    license="Apache 2.0",
    packages=setuptools.find_packages(),
    package_data={
        "turkish_treebanks": [
            "../data/web.conllu",
            "../data/wiki.conllu",
        ],
    },
    include_package_data=True,
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: Turkish",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    install_requires=["protobuf"],
    python_requires='>=3.7',
)
