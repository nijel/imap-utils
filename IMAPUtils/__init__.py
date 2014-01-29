# -*- coding: UTF-8 -*-
# vim: expandtab sw=4 ts=4 sts=4:
'''
Generic helper class for IMAP-utils.
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

__version__ = '0.5'

import sys
import imaplib
import time
import ConfigParser
import os
import codecs
from IMAPUtils.Codec import imap4_utf_7

codecs.register(imap4_utf_7)


class IMAPUtil(object):
    '''
    Wrapper class for IMAP utilities. It takes care about configuration
    and connecting to IMAP.
    '''
    def __init__(self):
        '''
        Reads configuration and prepares private variables defining
        simulation or verbose mode.
        '''
        path = os.path.expanduser('~/.imap-utils')
        self._config = ConfigParser.ConfigParser()
        # We want case sensitive names
        self._config.optionxform = str
        self._config.read(path)
        self._imap = None
        try:
            self._simulate = self._config.getboolean('IMAP', 'simulate')
        except ConfigParser.NoOptionError:
            self._simulate = False
        try:
            self._verbose = self._config.getboolean('IMAP', 'verbose')
        except ConfigParser.NoOptionError:
            self._verbose = False

    def login(self):
        '''
        Logins to IMAP server according to configuration.
        '''
        # Read connection settings
        host = self._config.get('IMAP', 'host')
        login = self._config.get('IMAP', 'login')
        password = self._config.get('IMAP', 'password')
        try:
            ssl = self._config.getboolean('IMAP', 'ssl')
        except ConfigParser.NoOptionError:
            ssl = False

        # Connect to server
        if ssl:
            self._imap = imaplib.IMAP4_SSL(host)
        else:
            self._imap = imaplib.IMAP4(host)

        # Login
        res = self._imap.login(login, password)
        if res[0] != 'OK':
            sys.stderr.write("login: %s\n" % str(res))
            sys.exit(1)

    def get_ints(self, section, name):
        '''
        Reads two ints from configuration.
        '''
        raw = self._config.get(section, name)
        if raw.find(',') == -1:
            return (int(raw), int(raw))
        raw_read, raw_unread = raw.split(',')
        return (int(raw_read), int(raw_unread))

    def get_timestamps(self, section, name):
        '''
        Reads two timestamp deltas from configuration.
        '''
        read, unread = self.get_ints(section, name)
        return (
            time.localtime(time.time() - (read * 86400)),
            time.localtime(time.time() - (unread * 86400))
        )
