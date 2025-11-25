#!/usr/bin/env python

from pathlib import Path

from setuptools import setup
from setuptools.extension import Extension
from Cython.Build import cythonize

from superfreq.setup_package import get_extensions


# Ensure the README is used as the long description if available
README = Path(__file__).with_name("README.rst")
if README.exists():
    long_description = README.read_text(encoding="utf-8")
else:
    long_description = None

extensions = cythonize(get_extensions(), language_level="3")

setup(
    ext_modules=extensions,
    long_description=long_description,
)
