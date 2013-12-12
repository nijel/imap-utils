IMAP Utils
==========

Collection of small script useful to manage IMAP account.

Homepage
========

<http://cihar.com/software/imap-utils/>

License
=======

GNU GPL version 3 or later.

Configuration
=============

All utils share ~/.imap-utils configuration file. IMAP connection is
configuration section:

    [IMAP]
    host = hostname ; Host where to connect
    login = user ; User name
    password = password ; Password
    ssl = 1 ; Whether to use SSL
    simulate = 1 ; Do not perform actions, only simulate
    verbose = 1 ; Print what is going on


imap-purge
==========

Purges old emails from defined folders. Configuration sections:

    [purge]
    folder = <read>,<unread> ; Purges mails in folder

    [purge-recursive]
    folder = <read>,<unread> ; Purges mails in folder and sub folders

Read mails are purged after <read> days, unread after <unread> days.


imap-folders
============

Creates folders on IMAP. Configuration sections:

    [create]
    folder = 1
    anotherfolder = 1


imap-stats
==========

Lists number of unread/unseen mails on IMAP.


store-message
=============

Stores message from stdin to folder defined by first argument.


process-messages
================

Reads all messages from folder (first argument) and passes them to
external program (second argument).


Bug reporting
=============

Please report found bugs to <https://github.com/nijel/imap-utils/issues>.


Version control
===============

Developed in Git on GitHub: https://github.com/nijel/imap-utils
