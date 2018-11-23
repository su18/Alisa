#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author : Su18
# @Copyright : <phoebebuffayfan9527@gmail.com>
# @For U : Like knows like.

import sys


def import_detect():
    """
    detect request module
    """
    try:
        import requests
        import urllib3
        urllib3.disable_warnings()
    except ImportError:
        not_found = 'Faltal Python module requests not found.'
        how_to_install = 'Try to install it with \"pip3 install -r requirements.txt\"'
        print('\033[31m☾ ❤ ☽ Alisa : %s (。﹏。) \033[0m' % not_found.center(62))
        print('\033[31m☾ ❤ ☽ Alisa : %s o(￣ε￣*) \033[0m' % how_to_install.center(62))
        sys.exit(1)
