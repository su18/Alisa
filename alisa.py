#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author : Su18
# @Copyright : <phoebebuffayfan9527@gmail.com>
# @For U : Like knows like.

import time
from core.logo import logo_print
from plugins.greeting import greeting
from plugins.import_detect import import_detect
from core.options import options
from core.api_spider import Spider
from plugins.url_format import get_url_protocol
from plugins.url_format import url_restrict
from core.scanner import dir_scan


# Print Logo
logo_print()

# Detect Modules
import_detect()

# Print Greeting
greeting()

# Define ArgumentParser Keyword
final_option = options()

# Get ArgumentParser Value
target = final_option.get('targets')
dict_file = './dict/' + final_option.get('dict')
user_agent = {'User-Agent': final_option.get('user_agent')}
cookies = final_option.get('cookies')
proxy = final_option.get('proxy')[0]
proxies = {'http': proxy, 'https': proxy}
delay = final_option.get('delay')
th_number = final_option.get('thread')
crawl_depth = final_option.get('crawl_depth')

# Format
url_protocol = get_url_protocol(target)
domain_url = url_restrict(target, url_protocol)

# API Spider
spider_start = 'Spider Start ... '
print('\033[31m☾ ❧ ☽ Alisa : %s \033[0m' % spider_start.center(62))
split_line = '  '
print(split_line.ljust(81, '-'))
spider = Spider(target, crawl_depth, domain_url, url_protocol, user_agent, cookies, proxies, delay)
spider.crawler(th_number)
print(split_line.ljust(81, '-'))
spider_finish = 'Spider Finished ... '
print('\033[31m☾ ❧ ☽ Alisa : %s \033[0m' % spider_finish.center(62))

# A Little Break
little_break = 'Hu~Hu~I\'m gonna need a little break~'
print('\033[34m☾ ❧ ☽ Alisa : %s \033[0m' % little_break.center(62))
time.sleep(10)
after_break = 'Whoops!Time\'s up!'
print('\033[34m☾ ❧ ☽ Alisa : %s \033[0m' % after_break.center(62))

# Scanner
scan_start = 'Scanner Start ... '
print('\033[31m☾ ❧ ☽ Alisa : %s \033[0m' % scan_start.center(62))
print(split_line.ljust(81, '-'))
print(' |' + str('Urls').center(59) + '|' + str('Status').center(20) + '|')
print(split_line.ljust(81, '-'))
dir_scan(target, dict_file, user_agent, cookies, proxies, delay)
print(split_line.ljust(81, '-'))
scan_finish = 'Scanner Finished ... '
print('\033[31m☾ ❧ ☽ Alisa : %s \033[0m' % scan_finish.center(62))

ask = 'I\'m all done!Do you get what you want?'
print('\033[36m☾ ❧ ☽ Alisa : %s \033[0m' % ask.center(62))
goodbye = 'Good Bye~'
print('\033[36m☾ ❧ ☽ Alisa : %s ( ﾟдﾟ)つBye\033[0m' % goodbye.center(62))