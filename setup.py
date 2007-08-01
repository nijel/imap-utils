#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# vim: expandtab sw=4 ts=4 sts=4:
'''
Setup script for installation of IMAP utils using distutils
'''
__author__ = 'Michal Čihař'
__email__ = 'michal@cihar.com'
__license__ = '''
Copyright (c) 2003 - 2007 Michal Čihař

This program is free software; you can redistribute it and/or modify it
under the terms of the GNU General Public License version 2 as published by
the Free Software Foundation.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
more details.

You should have received a copy of the GNU General Public License along with
this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
'''

import distutils.core
import IMAPUtils

distutils.core.setup(name="imap-utils",
    version = IMAPUtils.__version__,
    description = "IMAP utils",
    long_description = "Set of simple utilities for managing IMAP emails.",
    author = "Michal Čihař",
    author_email = "michal@cihar.com",
    maintainer = "Michal Čihař",
    maintainer_email = "michal@cihar.com",
    url = "http://cihar.com/software/imap-utils/",
    license = "GPL",
    classifiers = [
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
    packages = ['IMAPUtils'],
    scripts = ['imap-purge', 'imap-folders', 'imap-stats'],
    )
