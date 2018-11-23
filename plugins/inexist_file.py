#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author : Su18
# @Copyright : <phoebebuffayfan9527@gmail.com>
# @For U : Like knows like.


import requests
import hashlib

user_agent = {
    'user-agent': 'Mozilla/5.0 (compatible; Baiduspider-render/2.0; +http://www.baidu.com/search/spider.html)'
}
inexist_url = None
inexist_md5 = None
result = {}


def inexist_test(target):
    """
    inexist file detect,return a dict with status code,size,md5,content.
    if there was a redirection it will record the new url
    """
    global result
    a = '/alisascannerineexistfiledetect'
    target = target + a
    check = '404-Not Found Page checking mode on...'
    print('\033[34m☾ ❤ ☽ Alisa : %s \033[0m' % check.center(62))
    page = requests.get(target, headers=user_agent, verify=False)
    content = page.content
    result = {'code': str(page.status_code),
              'size': len(content),
              'md5': hashlib.md5(content).hexdigest(),
              'content': content,
              'location': None}
    if len(page.history) >= 1:
        result['location'] = page.url
    return result


def check_code(target):
    """
    request rest,record different response,print information.
    """
    global inexist_url
    global inexist_md5
    first_result = inexist_test(target)
    if first_result['code'] == '404':
        result_warning = 'Normal 404 status code,just fine.'
        print('\033[34m☾ ❤ ☽ Alisa : %s (๑¯∀¯๑)\033[0m' % result_warning.center(62))
    elif first_result['code'] == '302' or first_result['location']:
        inexist_url = first_result['location']
        result_warning = 'Inexist file return a 302 redirection.'
        print('\033[34m☾ ❤ ☽ Alisa : %s \033[0m' % result_warning.center(62))
        jump_warning = 'Jumping to\033[0m \033[33m%s\033[0m \033[34m' % inexist_url
        print('\033[34m☾ ❤ ☽ Alisa : %s （〃｀3′〃）\033[0m' % jump_warning.center(62))
    else:
        inexist_md5 = first_result['md5']
        result_warning = 'Can not analyze response other than 404 or 302.'
        print('\033[34m☾ ❤ ☽ Alisa : %s \033[0m' % result_warning)
        result_md5 = 'Maybe it\'s a customized 404 page.\033[0m \033[34mMD5:%s' % inexist_md5
        print('\033[34m☾ ❤ ☽ Alisa : %s \033[0m' % result_md5.center(62))
