#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author : Su18
# @Copyright : <phoebebuffayfan9527@gmail.com>
# @For U : Like knows like.

from googlesearch import search
from plugins.domain_resolve import *

dir_listing = 'site:' + domain + ' intitle:index of' + ' intext:Parent Directory'
conf_exposed = 'site:' + domain + ' ext:xml| ext:conf| ext:cnf| ext:reg| ext:inf| ext:rdp| ext:cfg| ext:txt| ext:ora| \
ext:ini| ext:txt| ext:dat| ext:cgi| ext:dll| ext:bkf| ext:ctl'
db_exposed = 'site:' + domain + ' ext:sql| ext:dbf| ext:mdb| ext:wdb'
log_exposed = 'site:' + domain + ' ext:log'
bk_exposed = 'site:' + domain + ' ext:bkf| ext:bkp| ext:bak| ext:old| ext:backup| ext:zip| ext:rar| ext:tar| \
ext:tar.gz| ext:tar.gz'
login_page = 'site:' + domain + ' intext:管理|后台|登陆|用户名|密码|验证码|系统|帐号|注册|admin|login|manage|manager| \
master|register'
sql_error = 'site:' + domain + ' intext:"sql syntax near"|intext:"syntax error has occurred"| \
intext:"incorrect syntax near"|intext:"unexpected end of SQL command"|intext:"Warning: mysql_connect()"| \
intext:"Warning: mysql_query()"|intext:"Warning: pg_connect()"'
doc_exposed = 'site:' + domain + ' ext:doc|ext:docx|ext:odt|ext:pdf|ext:rtf|ext:sxw|ext:psw|ext:ppt| \
ext:pptx|ext:pps|ext:csv'
black_page = 'site:' + domain + ' intest:博彩|澳门|反共|色情|百家乐|轮盘|时时彩|荷官|香港彩|娱乐城|性爱|大陆|共匪|楼凤| \
外围|良家|一夜情|交友|上门服务|裸聊|找小姐|返水|自拍|六合彩|同城交友|丝袜|少妇|同城|小姐|狼友|桑拿|夜生活|真人娱乐|真钱|娱乐城| \
抽奖|免费试玩|随时结算|老虎机|真人娱乐|返点|德州扑克|棋牌|进入直播|游戏账号|VIP俱乐部|菠菜'
webshell_page = 'site:' + domain + ' intest:剑眉大侠|不灭之魂|仗剑孤行|通杀版|法客论坛|冰源|上传的口令|导出DLL文件出错| \
token虚拟机管理|老子的绝对路径|免杀版|提升权限|法克|后门|木马|小马|大马|脱库|黑客|一句话后门|挂马|清马|扫描IP|开放端口|提权| \
执行命令|设置密码|一句话木马|过狗|安全狗|K8飞刀|K8拉登哥哥|K8搞基大队'
all_hack = [
    {'all_hack_key': dir_listing, 'results': []},
    {'dir_listing': conf_exposed, 'results': []},
    {'db_exposed': db_exposed, 'results': []},
    {'log_exposed': log_exposed, 'results': []},
    {'bk_exposed': bk_exposed, 'results': []},
    {'login_page': login_page, 'results': []},
    {'sql_error': sql_error, 'results': []},
    {'doc_exposed': doc_exposed, 'results': []},
    {'black_page': black_page, 'results': []},
    {'webshell_page': webshell_page, 'results': []},
]
all_hack_key = ['dir_listing', 'dir_listing', 'db_exposed', 'log_exposed', 'bk_exposed', 'login_page', 'sql_error',
                'doc_exposed', 'black_page', 'webshell_page']


def google_hack():
    """
    search different sensitive dirs and record top 10 results using google hack
    """
    global all_hack
    print('\033[34m☾ ❤ ☽ Alisa : Google hack checking mode on...\033[0m')
    try:
        for i in range(0, 10):
            print('Checking %s module' % all_hack_key[i])
            for url in search(all_hack[i][all_hack_key[i]], stop=10):
                print('\033[34mInteresting url:\033[0m \033[33m%s\033[0m' % url)
                all_hack[i]['results'].append(url)
    except Exception as e:
        print('\033[31m☾ ❤ ☽ Alisa : %s,skip the module! |(*′口`)\033[0m' % e)
