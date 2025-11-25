"""Build configuration for superfreq extension modules."""

from setuptools import Extension


def get_extensions():
    # Import numpy lazily to avoid importing it at module load time when it may
    # not yet be installed (e.g. during build isolation).
    import numpy as np

    common_include_dirs = [np.get_include(), "cextern"]

    naff_extension = Extension(
        name="superfreq._naff",
        sources=["superfreq/_naff.pyx", "cextern/brent.c", "cextern/simpson.c"],
        include_dirs=common_include_dirs,
    )

    simpsgauss_extension = Extension(
        name="superfreq.simpsgauss",
        sources=["superfreq/simpsgauss.pyx", "cextern/simpson.c"],
        include_dirs=common_include_dirs,
    )

    return [naff_extension, simpsgauss_extension]
