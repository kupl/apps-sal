# cook your dish here
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 23:13:37 2020

@author: SRILEKHA
"""


for _ in range(int(input())):
    num = int(input())
    length = list(map(int, input().split()))
    temp = []
    ls = []
    for i in length:
        if i not in temp:
            temp.append(i)
    temp.sort()
    for j in temp:
        indices = []
        for k in range(0, num):
            if length[k] == j:
                if k - 1 not in indices:
                    indices.append(k)
        ls.append(len(indices))
    print(temp[ls.index(max(ls))])
