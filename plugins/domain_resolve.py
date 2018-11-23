#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author : Su18
# @Copyright : <phoebebuffayfan9527@gmail.com>
# @For U : Like knows like.

import socket
from urllib.parse import urlparse

domain = ''


def domain_resolve(target_url):
    """
    domain resolve test
    """
    global domain
    domain = urlparse(target_url).hostname
    target_loaded = 'Target\033[0m \033[33m%s\033[0m \033[34mhas been loaded.' % domain
    print('\033[34m☾ ✢ ☽ Alisa : %s *(੭*ˊᵕˋ)੭*\033[0m' % target_loaded.center(80))
    try:
        if socket.gethostbyname(domain):
            pass
    except Exception as e:
        print('\033[31m☾ ❤ ☽ Alisa : %s o(TヘTo)\033[0m' % str(e).center(62))
