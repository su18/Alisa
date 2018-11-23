#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author : Su18
# @Copyright : <phoebebuffayfan9527@gmail.com>
# @For U : Like knows like.

import time
import requests
from plugins.url_format import edit_url_end

exist_url = []
redirect_url = []
forbidden_url = []


def print_result(line, status_code):
    print(' |' + str(line).center(59) + '|' + str(status_code).center(20) + '|')


def head_url(target, user_agent, cookies, proxies):
    try:
        r = requests.head(target, timeout=2, headers=user_agent, cookies=cookies, proxies=proxies)
        return r.status_code
    except:
        pass


def dir_scan(target, dict_file, user_agent, cookies, proxies, delay):
    if len(target):
        with open(dict_file, "r", encoding='utf-8') as f:
            for line in f.readlines():
                line = line.strip("\n")
                target = edit_url_end(target)
                line = target + "/" + line
                status_code = head_url(line, user_agent, cookies, proxies)
                time.sleep(delay)
                if status_code == 200:
                    exist_url.append(line)
                    print_result(line, status_code)
                elif status_code == 302:
                    redirect_url.append(line)
                    print_result(line, status_code)
                elif status_code == 403:
                    forbidden_url.append(line)
                    print_result(line, status_code)
                else:
                    pass
