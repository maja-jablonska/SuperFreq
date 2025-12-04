#!/usr/bin/env python

from pathlib import Path

from importlib import util
from setuptools import setup
from setuptools.extension import Extension
from Cython.Build import cythonize


def _load_setup_helpers():
    setup_pkg_path = Path(__file__).parent / "superfreq" / "setup_package.py"
    spec = util.spec_from_file_location("superfreq_setup_package", setup_pkg_path)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load build configuration from superfreq/setup_package.py")
    module = util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# Ensure the README is used as the long description if available
README = Path(__file__).with_name("README.rst")
if README.exists():
    long_description = README.read_text(encoding="utf-8")
else:
    long_description = None

helpers = _load_setup_helpers()
extensions = cythonize(helpers.get_extensions(), language_level="3")

setup(
    ext_modules=extensions,
    long_description=long_description,
)
