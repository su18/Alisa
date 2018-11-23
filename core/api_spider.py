#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author : Su18
# @Copyright : <phoebebuffayfan9527@gmail.com>
# @For U : Like knows like.

import re
import requests
import time
import threading
from core.link_queue import LinkQueue
from plugins.url_format import edit_url_end
import urllib.parse

threads_pool = []
crawl_result = []


def get_domain(target):
    proto, rest = urllib.parse.splittype(target)
    host, rest = urllib.parse.splithost(rest)
    return host


class Spider(object):

    def __init__(self, target, crawl_depth, domain_url, url_protocol, user_agent, cookies, proxies, delay):
        self.LinkQueue = LinkQueue()
        self.LinkQueue.add_unvisited_url(target)
        self.crawl_depth = crawl_depth
        self.domain_url = domain_url
        self.url_protocol = url_protocol
        self.current_depth = 1
        self.user_agent = user_agent
        self.cookies = cookies
        self.proxies = proxies
        self.delay = delay

    def get_page_links(self, target):
        url_links = []
        page_source = requests.get(target, headers=self.user_agent, cookies=self.cookies, proxies=self.proxies).text
        page_links1 = re.findall(
            r'(?<=href=\").*?(?=\")|(?<=href=\').*?(?=\')|(?<=src=\").*?(?=\")|(?<=src=\').*?(?=\')',
            page_source.lower())
        for m in page_links1:
            if ".jpg" not in m and ".jpeg" not in m and ".png" not in m and ".gif" not in m and ".mp4" not in m \
                    and ".avi" not in m and ".swf" not in m and ".flv" not in m and ".ico" not in m \
                    and "javascript" not in m:
                url_links.append(m)
        page_links2 = re.findall(
            r'(http[^\s]:*?(\.html|\.jhtml|\.js|\.json|\.amsx|\.wsdl|\.xml|\.jsp|\.php|\.asp|\.aspx))',
            page_source.lower())
        for n in range(0, len(page_links2)):
            if page_links2[n][0] not in url_links:
                url_links.append(page_links2[n][0])
        return url_links

    def process_url(self, target):
        domain_url = self.domain_url
        url_protocol = self.url_protocol
        true_url = []
        process_target = ""
        for line in self.get_page_links(target):
            line = edit_url_end(line)
            if line not in true_url:
                process_domain = get_domain(line)
                if process_domain:
                    if domain_url in process_domain:
                        try:
                            r = requests.get(process_target, timeout=3, headers=self.user_agent,
                                             cookies=self.cookies, proxies=self.proxies)
                            status_code = r.status_code
                            if status_code == 200:
                                true_url.append(line)
                        except:
                            pass

                else:
                    if '://' not in line:
                        process_target = url_protocol + '://' + domain_url + line
                        try:
                            r = requests.get(process_target, timeout=3,  headers=self.user_agent,
                                             cookies=self.cookies, proxies=self.proxies)
                            status_code = r.status_code
                            if status_code == 200:
                                true_url.append(process_target)
                        except:
                            pass
        return true_url

    def collect_visited_url(self):
        while not self.LinkQueue.unvisited_url_empty():
            visited_url = self.LinkQueue.pop_unvisited_url()
            crawled_urls = 'Crawled Url:'
            print(' |' + crawled_urls.center(19) + '|  ' + str(visited_url).ljust(58) + '|')
            if visited_url is None or visited_url == '':
                continue
            crawl_result.append(visited_url)
            links = self.process_url(visited_url)
            self.LinkQueue.add_visited_url(visited_url)
            for link in links:
                self.LinkQueue.add_unvisited_url(link)

    def crawler(self, th_number):
        global threads_pool
        while self.crawl_depth >= self.current_depth:
            for i in range(th_number):
                t = threading.Thread(target=self.collect_visited_url)
                threads_pool.append(t)
            for i in range(th_number):
                threads_pool[i].start()
                time.sleep(1)
            for i in range(th_number):
                threads_pool[i].join()
            self.current_depth += 1
        return self.LinkQueue.visited
