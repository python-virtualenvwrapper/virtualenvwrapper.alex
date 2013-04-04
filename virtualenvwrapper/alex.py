#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2013 Doug Hellmann.  All rights reserved.
#
"""Define aliases for common typos for virtualenvwrapper commands.
"""

import logging
import subprocess

log = logging.getLogger('virtualenvwrapper.alex')

def initialize_source(args):
    """Installs aliases
    """
    return """
alias wokr=workon
"""
