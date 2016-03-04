#!/usr/bin/env python

from setuptools import setup

setup(name='varconvolve',
      version='1.0',
      description='Convolution with a kernel with a variable width',
      author='Janez Kos',
      author_email='jkos@physics.usyd.edu.au',
      py_modules=['varconvolve'],
      install_requires=['numpy', 'scipy'],
     )