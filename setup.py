#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
import os
from setuptools import find_packages
from numpy.distutils.core import setup, Extension

try:
    with open('README.md') as f:
        readme = f.read()
except IOError:
    readme = ''

def _requires_from_file(filename):
    return open(filename).read().splitlines()

extensions = []
setup(
    name="PuzzleImage",
    version="0.0.1",
    url='https://github.com/MakePuzz/PuzzleImage',
    author='The puzzle-japan Team',
    author_email='puzzle.hokkaido@gmail.com',
    maintainer='MakePuzz',
    maintainer_email='puzzle.hokkaido@gmail.com',
    description='A Python library to make puzzle images',
    long_description=readme,
    packages=find_packages(),
    ext_modules=extensions,
    install_requires=_requires_from_file('requirements.txt'),
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
    ]
)