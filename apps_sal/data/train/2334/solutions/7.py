from math import *
from bisect import *
from collections import *
from random import *
from decimal import *
from itertools import *
import sys
input=sys.stdin.readline
def inp():
    return int(input())
def st():
    return input().rstrip('\n')
def lis():
    return list(map(int,input().split()))
def ma():
    return list(map(int,input().split()))
t=inp()
while(t):
    t-=1
    s=st()
    stack=[]
    for i in range(len(s)):
        stack.append(s[i])
        while(len(stack)!=0 and len(stack)-1):
            x=stack[-1]
            y=stack[-2]
            if(x==y=='B' or (x=='B' and y=='A')):
                stack.pop()
                stack.pop()
            else:
                break
    print(len(stack))

