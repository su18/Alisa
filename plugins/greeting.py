#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author : Su18
# @Copyright : <phoebebuffayfan9527@gmail.com>
# @For U : Like knows like.

import time


def greeting():
    """
    print different greetings base on time
    """
    midnight = 'It\'s midnight,dear. Why would you wake me up... ZZzz…'
    morning = 'Time for work! Let\'s do this.'
    afternoon = 'Good afternoon. I just had a nap,feel good to scan some webs.'
    evening = 'Now is off-duty time. You better make it quick!'
    sunrise = 'Morning~ Seems like someone is a hard-working bee~.'
    a = int(time.strftime("%H", time.localtime()))
    if 23 >= a >= 18:
        print('\033[32m☾ ☠ ☽ Alisa : %s (*￣︿￣)\033[0m' % evening.center(62))
    elif 18 > a >= 12:
        print('\033[32m☾ ☺ ☽ Alisa : %s |･ω･｀)\033[0m' % afternoon.center(62))
    elif 7 >= a >= 5:
        print('\033[32m☾ ♨ ☽ Alisa : %s (｡･∀･)ﾉﾞ\033[0m' % sunrise.center(62))
    elif 12 > a > 7:
        print('\033[32m☾ ☼ ☽ Alisa : %s <(￣ˇ￣)/\033[0m' % morning.center(62))
    else:
        print('\033[32m☾ ☪ ☽ Alisa : %s (。-ω-)\033[0m' % midnight.center(62))
