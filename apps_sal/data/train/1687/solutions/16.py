'''
    Auther: ghoshashis545 Ashis Ghosh
    College: jalpaiguri Govt Enggineering College

'''
from os import path
import sys
from functools import cmp_to_key as ctk
from collections import deque,defaultdict as dd 
from bisect import bisect,bisect_left,bisect_right,insort,insort_left,insort_right
from itertools import permutations
from datetime import datetime
from math import ceil,sqrt,log,gcd
def ii():return int(input())
def si():return input()
def mi():return map(int,input().split())
def li():return list(mi())
abc='abcdefghijklmnopqrstuvwxyz'
abd={'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
mod=1000000007
#mod=998244353
inf = float("inf")
vow=['a','e','i','o','u']
dx,dy=[-1,1,0,0],[0,0,1,-1]

def bo(i):
    return ord(i)-ord('a')


def solve():
    
    for _ in range(ii()):
        
        n,k = mi()
        if k==3:
            print(1,7)
            print(7,3)
            print(3,1)
        if k==4:
            print(1,7)
            print(7,3)
            print(3,6)
            print(6,1)
        if k==5:
            print(0,1)
            print(1,3)
            print(3,5)
            print(5,7)
            print(7,0)
        if k==6:
            print(0,1)
            print(1,2)
            print(2,3)
            print(3,5)
            print(5,7)
            print(7,0)
        if k==7:
            print(5,3)
            print(1,7)
            print(0,4)
            print(2,5)
            print(3,1)
            print(4,2)
            print(7,0)
        if k==8:
            print(5,6)
            print(0,4)
            print(2,5)
            print(3,1)
            print(4,2)
            print(1,7)
            print(6,0)
            print(7,3)
            continue
        if k == pow(2,n):
            x = [[] for i in range(n+1)]
            for i in range(1<<n):
                c = 0
                for j in range(n):
                    if(i>>j)&1:
                        c+=1
                x[c].append(i)
            
            dq = deque([0])
            for i in range(n):
                a = x[i]
                b = x[i+1]
                if len(a) <= len(b):
                    for j in range(len(a)):
                        print(a[j],b[j])
                    for j in range(len(a),len(b)):
                        dq.append(b[j])
                else:
                    for j in range(len(b)):
                        print(a[j],b[j])
                    x2 = len(b)
                    for j in range(len(b),len(a)):
                        if len(dq)==0:
                            break
                        x1 = dq[0]
                        dq.popleft()
                        print(a[j],x1)
                        x2+=1
                    for j in range(x2,len(a)):
                        dq.append(a[j])
            print(x[-1][0],dq[0])

            
            
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
        
        
def __starting_point():
    solve()

__starting_point()
