#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import find_packages
from distutils.core import setup

setup(
    author=u'Matthew Fisher',
    author_email='bacongobbler@bacongobbler.com',
    name='python-stackato',
    description='Python interface to Stackato',
    version="0.1",
    url='http://www.github.com/bacongobbler/python-stackato/',
    license='MIT License',
    packages = find_packages(),
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    install_requires=[
        open("requirements.txt").readlines(),
    ],
)
