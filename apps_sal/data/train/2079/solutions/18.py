#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 23:50:55 2020

@author: shailesh
"""


from collections import defaultdict


def find_cost(node_1,node_2,intersect_dict):
    new_dict = defaultdict(lambda : 0)
    cost = 0
    while node_1 != 0:
        new_dict[node_1] = 1
        cost+= intersect_dict[node_1]
#        print(node_1,cost)
        node_1 //= 2
    
    while node_2!=0:
        if new_dict[node_2]:
            cost -= intersect_dict[node_2]
#            print(node_2)
            break
        else:
            new_dict[node_2] = 1
            cost += intersect_dict[node_2]
            node_2 //= 2
#            print(node_2,cost)
    while node_2 != 0:
        node_2 //= 2
        cost -= intersect_dict[node_2]
        
    
    return cost


def increase_cost_on_path(node_1,node_2,inc_cost,intersect_dict):
    new_dict = defaultdict(lambda :0)
    while node_1 != 0:
        new_dict[node_1] = 1
        intersect_dict[node_1] += inc_cost
        node_1 //= 2
    while node_2 != 0 :
        if new_dict[node_2]:
            break
        else:
            intersect_dict[node_2] += inc_cost
            node_2//=2
        
    while node_2 != 0:
        intersect_dict[node_2] -= inc_cost
        node_2 //= 2
    return intersect_dict


Q = int(input())

#arr = [0 for i in range(n+1)]

intersect_dict = defaultdict(lambda : 0)

for q in range(Q):
    query = [int(i) for i in input().split()]
    if query[0] == 1:
        v,u,w = query[1:]
        intersect_dict = increase_cost_on_path(v,u,w,intersect_dict)
    else:
        v,u = query[1:]
        cost = find_cost(u,v,intersect_dict)
        print(cost)
    

