#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
doclink = """
Documentation
-------------

The full documentation is at http://ytrie.rtfd.org."""
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='ytrie',
    version='0.1.0',
    description='A pure python API for Trie data access',
    long_description=readme + '\n\n' + doclink + '\n\n' + history,
    author='Ashwin Venkatesan',
    author_email='ashwinjv@gmail.com',
    url='https://github.com/ashwinjv/ytrie',
    packages=[
        'ytrie',
    ],
    package_dir={'ytrie': 'ytrie'},
    include_package_data=True,
    install_requires=[
    ],
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords='ytrie',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
