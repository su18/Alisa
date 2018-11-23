#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author : Su18
# @Copyright : <phoebebuffayfan9527@gmail.com>
# @For U : Like knows like.

import re
from plugins.domain_resolve import domain_resolve


def get_url_protocol(target_url):
    return re.findall(r".*(?=://)", target_url)[0]


def url_format(target_url):
    """
    format target url adding http:// and /
    """
    if target_url.startswith('http://') or target_url.startswith('https://'):
        pass
    else:
        target_url = 'http://' + target_url
    target_url = edit_url_end(target_url)
    domain_resolve(target_url)
    return target_url


def edit_url_end(target_url):
    """
    消除/和锚点引起的重复
    """
    if target_url:
        if target_url.endswith("/"):
            target_url = target_url[:-1]
        if '#' in target_url:
            index = target_url.index('#')
            target_url = target_url[:index]
    return target_url


def url_restrict(target_url, url_protocol):
    target_url = target_url.replace(url_protocol + "://", "")
    if not re.findall(r"^www", target_url):
        same_url = "www." + target_url
        if same_url.find("/") != -1:
            same_url = re.findall(r"(?<=www.).*?(?=/)", same_url)[0]
        else:
            same_url = same_url + "/"
            same_url = re.findall(r"(?<=www.).*?(?=/)", same_url)[0]
    else:
        if target_url.find("/") != -1:
            same_url = re.findall(r"(?<=www.).*?(?=/)", target_url)[0]
        else:
            same_url = target_url + "/"
            same_url = re.findall(r"(?<=www.).*?(?=/)", same_url)[0]
    return same_url
