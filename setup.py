# -*- coding: utf-8 -*-
"""
    Pixela
    ~~~~~~

    Pixela API client for Python.


    `Ruby pixela client <https://github.com/sue445/pixela>`_


    :copyright: (c) 2018 Shinya Ohyanagi, All rights reserved.
    :license: BSD, see LICENSE for more details.
"""
import os

from setuptools import (
    find_packages,
    setup,
)

from pixela import __version__

requires = ['requests', 'pytz']

app_name = 'pixela'

rst_path = os.path.join(os.path.dirname(__file__), 'README.rst')
description = ''
with open(rst_path) as f:
    description = f.read()

setup(
    name=app_name,
    version=__version__,
    author='Shinya Ohyanagi',
    author_email='sohyanagi@gmail.com',
    url='http://github.com/heavenshell/py-pixela',
    description='Pixela API client for Python.',
    long_description=description,
    license='BSD',
    platforms='any',
    packages=find_packages(exclude=['tests']),
    package_dir={'': '.'},
    install_requires=['mock', 'requests', 'pytz'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    tests_require=requires,
    test_suite='tests',
)
