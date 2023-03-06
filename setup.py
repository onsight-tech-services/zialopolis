"""Zialopolis setup script."""
#!/usr/bin/env python

import logging
import os
import sys
from glob import glob
from argparse import ArgumentParser

try:
    from Cython.Distutils.extension import Extension
    from Cython.Distutils import build_ext
    from setuptools import setup
except ImportError:
    from setuptools import setup, Extension
    USING_CYTHON = False
else:
    USING_CYTHON = True

FILE_EXTENSION = 'pyx' if USING_CYTHON else 'c'
sources = glob(f'zialopolis/*.{FILE_EXTENSION}')
extensions = [
    Extension(
        source.split('.')[0].replace(os.path.sep, '.'),
        sources=[source]
    ) for source in sources
]
cmdclass = {'build_ext': build_ext} if USING_CYTHON else {}

PARSER = ArgumentParser(
    prog='Zialopolis',
    description='Zialopolis setup script.'
)
PARSER.add_argument(
    'peer',
    help='The peer to build for. (e.g. "node" or "client")'
)

if __name__ == "__main__":
    args = PARSER.parse_args()
    if args.peer not in ('node', 'client'):
        logging.error("Invalid peer '%s' specified.", args.peer)
        sys.exit(1)
    setup(
        name=f'Zialopolis {args.peer}',
        version='0.1',
        description='Zialopolis, the neverending city.',
        author='OnSight Tech Services LLC',
        author_email='info@onsight.services',
        ext_modules=extensions,
        cmdclass=cmdclass,
        requires=[
            "numpy",
            "sqlalchemy",
            "Cython>=3.0.0b1"
        ]
    )
