#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 16:14:34 2016

@author: kostiantyn.omelianchuk
"""

from sys import stdin, stdout
lines = stdin.readlines()
n = int(lines[0])
a = [int(x)  for x in lines[1].split()]
b = [int(x)  for x in lines[2].split()]

check_array = [0 for i in range(n)]
snm = [i for i in range(n)]
r = [1 for i in range(n)]
sums = dict(list(zip(list(range(n)), a)))    

def find_x(x):
    if snm[x] != x:
        snm[x] = find_x(snm[x])
    return snm[x]


def union(x_start, y_start):
    x = find_x(x_start)
    y = find_x(y_start)
    sums[x] += sums[y]
    sums[y] = sums[x]
    if x == y:
        return x
        #sums[x] += sums[x_start]
    if r[x] == r[y]:
        r[x] += 1
    if r[x] < r[y]:
        snm[x] = y
        return y
    else:
        snm[y] = x
        return x
    

max_list = []
total_max = 0

for i in range(n):
    cur_sum = 0
    flag = 0
    
    max_list.append(total_max)
    #pos = n-i-1

    elem = b[n-i-1] - 1
    check_array[elem] = 1
    #pos_x = find_x(elem)
    if elem>0:
        if check_array[elem-1] == 1:
            pos = union(elem-1,elem)
            cur_sum = sums[pos]
            #print(sums, check_array, total_max, cur_sum, elem, find_x(elem))
            
        else:
            flag += 1
    else:
        flag += 1
    if elem<(n-1):
        if check_array[elem+1] == 1:
            pos = union(elem,elem+1)
            cur_sum = sums[pos]
            #print(sums, check_array, total_max, cur_sum, elem, find_x(elem))
            
        else:
            flag += 1
    else:
        flag += 1
    if flag == 2:
        total_max = max(total_max,sums[elem])
    else:
        total_max = max(cur_sum, total_max)
    
        
max_list.append(total_max)

for j in range(1,n+1):
    print(max_list[n-j])
    
    
    
    
    

