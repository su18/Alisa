#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author : Su18
# @Copyright : <phoebebuffayfan9527@gmail.com>
# @For U : Like knows like.

import requests


def robots_url(target):
    """
    discover robots.txt and add path to list
    """
    robots_txt = []
    try:
        result = requests.get(target + 'robots.txt')
        if not result.status_code == 200:
            return
        for line in result.text.splitlines():
            if line.startswith('Disallow:') or line.startswith('Allow:'):
                if len(line.split(':')) > 1:
                    robots_txt.append(line.split(':')[1])
        return list(set(robots_txt))
    except Exception as e:
        print('\033[31m☾ ❤ ☽ Alisa : Something went wrong getting robots.txt! |(*′口`)\033[0m')
        print('\033[31m☾ ❤ ☽ Alisa : %s |(*′口`)\033[0m' % e)
        return None
