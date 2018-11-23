#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Author : Su18
# @Copyright : <phoebebuffayfan9527@gmail.com>
# @For U : Like knows like.


class LinkQueue(object):
    """
    store visited and unvisited urls in list
    """
    def __init__(self):
        self.visited = []
        self.unvisited = []

    def get_visited_url(self):
        return self.visited

    def get_unvisited_url(self):
        return self.unvisited

    def add_visited_url(self, target):
        if target != '' and target not in self.visited:
            return self.visited.append(target)

    def add_unvisited_url(self, target):
        if target != '' and target not in self.visited and target not in self.unvisited:
            return self.unvisited.insert(0, target)

    def pop_unvisited_url(self):
        try:
            return self.unvisited.pop()
        except Exception as e:
            print(e)
            return None

    def unvisited_url_empty(self):
        return len(self.unvisited) == 0
