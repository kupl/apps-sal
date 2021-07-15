# Target - Expert on CF
# Be Humblefool

import sys

# inf = float("inf")
sys.setrecursionlimit(10000000)

# abc='abcdefghijklmnopqrstuvwxyz'
# abd={'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
# mod, MOD = 1000000007, 998244353
# words = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'quarter',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',21:'twenty one',22:'twenty two',23:'twenty three',24:'twenty four',25:'twenty five',26:'twenty six',27:'twenty seven',28:'twenty eight',29:'twenty nine',30:'half'}
# vow=['a','e','i','o','u']
# dx,dy=[0,1,0,-1],[1,0,-1,0]

# import random
from collections import deque, Counter, OrderedDict,defaultdict
# from heapq import nsmallest, nlargest, heapify,heappop ,heappush, heapreplace
# from math import ceil,floor,log,sqrt,factorial,pi,gcd
# from bisect import bisect,bisect_left,bisect_right,insort,insort_left,insort_right

def get_array(): return list(map(int, sys.stdin.readline().strip().split()))
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def input(): return sys.stdin.readline().strip()

def dfs(current_node, xor, change_zero, change_one):
    stack = [(current_node,xor,change_zero,change_one)]
    nonlocal visited,ans,store

    while stack:
        current_node,xor,change_zero,change_one = stack.pop()
        visited[current_node-1] = True
        if xor==0:
            if change[current_node-1]!=current[current_node-1]:
                if ~change_zero&1:
                    change_zero+=1
                    ans+=1
                    store.append(current_node)
            else:
                if change_zero&1:
                    change_zero+=1
                    ans+=1
                    store.append(current_node)
        else:
            if change[current_node-1]!=current[current_node-1]:
                if ~change_one&1:
                    change_one+=1
                    ans+=1
                    store.append(current_node)
            else:
                if change_one&1:
                    change_one+=1
                    ans+=1
                    store.append(current_node)
        new_xor = xor^1
        for child in mydict[current_node]:
            if not visited[child-1]:
                stack.append((child, new_xor, change_zero, change_one))




n = int(input())
mydict = defaultdict(list)
for i in range(n-1):
    x,y = get_ints()
    mydict[x].append(y)
    mydict[y].append(x)

current = get_array()
change = get_array()

# change_zero,change_one = 0,0
ans = 0
current_node = 1
store = []
visited = [False]*(n)
dfs(current_node,1,0,0)
print(ans)
for i in store:
    print(i)
