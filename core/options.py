#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author : Su18
# @Copyright : <phoebebuffayfan9527@gmail.com>
# @For U : Like knows like.

import sys
import argparse
from plugins.url_format import url_format
from plugins.inexist_file import *


def options():
    """
    get user's options and return
    """
    default_ua = 'Mozilla/5.0 (compatible; Baiduspider-render/2.0; +http://www.baidu.com/search/spider.html)'
    usage = 'python3 alisa.py -u url -d dict [options]'
    description = '''
    Alisa is a Web Directory Scanner.
    She can help you discover the sensitive documents in websites.
    She is the very first Python script that I write since I learn.
    I believe she doesn't see much of the world herself.
    So,treat her well,gentleman.
    '''
    epilog = 'Please note that this product is prohibited from being used illegally.'
    parser = argparse.ArgumentParser(
        usage=usage, description=description, epilog=epilog, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-C', dest='cookies', help="Customized cookies (e.g: key:value)", default="")
    parser.add_argument('-P', dest='proxies', help="Use http/https proxy (e.g: http://127.0.0.1:1080)", default="")
    parser.add_argument('-T', dest='request_delay', help="Time delay between requests (e.g: 0.25 or 1.75)", default=0)
    parser.add_argument('-a', dest='user_agent', help="Customized UA (default Baidu-Spider UA)", default=default_ua)
    parser.add_argument('-c', dest='crawl_depth', help="Crawl Depth(default 1)", default=1)
    parser.add_argument('-d', dest='dict', help="Dictionary list （e.g: php.txt,asp.txt,...default none)", default="")
    parser.add_argument('-g', dest='google_hack', help="Discover sensitive dir by google hack ", default=False)
    parser.add_argument('-t', dest='threads', type=int, help="Customized threads (default 5)", default=5)
    parser.add_argument('-u', dest='target', help="Target url", default=None)
    args = parser.parse_args()

    # Default Display
    if not args.target:
        none_url = 'How can I scan a website when you don\'t give me an url?'
        tips = 'Use -h or --help to show the usage!'
        print('\033[31m☾ ❤ ☽ Alisa : %s (。﹏。) \033[0m' % none_url.center(62))
        print('\033[34m☾ ❤ ☽ Alisa : %s (￣︶￣)↗ \033[0m' % tips.center(62))
        sys.exit()

    # Format Url And Domain Resolv
    target = url_format(args.target)

    # Detect What Inexist File Looks Like
    check_code(target)

    # Google hack
    google_hack = args.google_hack
    if google_hack:
        google_hack_on = 'Google hack mode on...'
        print('\033[34m☾ ❤ ☽ Alisa :  %s\033[0m' % google_hack_on.center(62))
    option = {"thread": int(args.threads),
              "delay": args.request_delay,
              "cookies": args.cookies,
              "targets": target,
              "user_agent": args.user_agent,
              "crawl_depth": int(args.crawl_depth),
              "dict": args.dict,
              "proxy": args.proxies.split(','),
              "google_hack": google_hack}
    return option
