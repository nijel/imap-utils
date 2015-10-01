#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# vim: expandtab sw=4 ts=4 sts=4:
'''
Setup script for installation of IMAP utils using distutils
'''
__author__ = 'Michal Čihař'
__email__ = 'michal@cihar.com'
__license__ = '''
Copyright (c) 2003 - 2014 Michal Čihař

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

from setuptools import setup
import IMAPUtils

setup(
    name="imap-utils",
    version=IMAPUtils.__version__,
    description="IMAP utils",
    long_description="Set of simple utilities for managing IMAP emails.",
    author=u"Michal Čihař",
    author_email="michal@cihar.com",
    maintainer=u"Michal Čihař",
    maintainer_email="michal@cihar.com",
    platforms=['Linux', 'Mac OSX', 'Windows XP/2000/NT', 'Windows 95/98/ME'],
    keywords=['IMAP', 'mail', 'email'],
    url="http://cihar.com/software/imap-utils/",
    download_url="http://cihar.com/software/imap-utils/",
    license="GPL",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Communications :: Email',
        'Topic :: Utilities',
    ],
    packages=['IMAPUtils'],
    scripts=[
        'imap-purge',
        'imap-folders',
        'imap-stats',
        'fetch-messages',
        'process-messages',
        'store-message',
    ],
)
