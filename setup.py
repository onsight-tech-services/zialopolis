"""Zialopolis setup script."""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

# from Cython.Distutils.extension import Extension
# from Cython.Distutils import build_ext
from setuptools import setup, find_packages
# except ImportError:
#     logging.info('Cython not found, falling back to C.')
#     from setuptools import setup, Extension
#     USING_CYTHON = False
# else:
#     USING_CYTHON = True

# sources = glob(f'zialopolis_{os.getenv("PEER")}/*.pyx')
# extensions = list()
# for (path, directories, filenames) in os.walk(f'zialopolis_{os.getenv("PEER")}'):
#     for filename in filenames:
#         if filename.endswith('.pyx'):
#             extensions.append(
#                 Extension(
#                     filename.split('.')[0],
#                     sources=[os.path.join(path, filename)]
#                 )
#             )

setup(
    name='zialopolis',
    version='0.1',
    description='Zialopolis, the neverending city.',
    author='OnSight Tech Services LLC',
    author_email='info@onsight.services',
    packages=find_packages(),
    # ext_modules=extensions,
    # cmdclass={'build_ext': build_ext},
    install_requires=[
        "numpy",
        "sqlalchemy",
        # "Cython>=3.0.0b1",
        "mongoengine>=0.20.0",
    ]
)
