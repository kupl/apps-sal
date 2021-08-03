# cook your dish here
# Coding is about expressing your feeling and
# there is always a better way to express your feeling _Deepak
import sys
# sys.stdin=open('input.txt','r')
# sys.stdout=open('output.txt','w')
from sys import stdin, stdout
from collections import deque, defaultdict
from math import ceil, floor, inf, sqrt, factorial, gcd, log2
from copy import deepcopy
def ii1(): return int(stdin.readline().strip())
def is1(): return stdin.readline().strip()


def iia(): return list(map(int, stdin.readline().strip().split()))
def isa(): return stdin.readline().strip().split()


mod = 1000000007
# s=is1()
# n = len(s)
# count,res,flag,subans=1,0,0,1
# subcount=0
# for i in range(0,n-1):
#     if s[i]=='c' or s[i]=='k':
#         flag=1
#         break
#     if s[i]==s[i+1] and (s[i]=='f' or s[i]=='g'):
#         count+=1
#     elif count>1:
#         subans*=(count*(count-1))//2
#         count=1
#         subcount+=1
# if s[-1]=='c' or s[-1]=='k':
#     flag=1
# elif count>1:
#     subans*=(count*(count-1))//2
#     subcount+=1
# if flag:
#     print(0)
# else:
#     res=(1<<(subcount-1))
#     res*=subans
#     print(res%mod)
n = ii1()
arr = [None] * n
for ii in range(n):
    arr[ii] = iia()
count = 2
if n == 1 or n == 2:
    print(n)
else:
    flag = [0] * n
    flag[0] = -1
    flag[-1] = 1
    for i in range(1, n - 1):
        if flag[i - 1] == -1:
            if arr[i][0] - arr[i - 1][0] > arr[i][1]:
                flag[i] = - 1
                count += 1
            elif arr[i + 1][0] - arr[i][0] > arr[i][1]:
                flag[i] = 1
                count += 1
        elif flag[i - 1] == 1:
            if arr[i][0] - (arr[i - 1][0] + arr[i - 1][1]) > arr[i][1]:
                flag[i] = -1
                count += 1
            elif arr[i + 1][0] - arr[i][0] > arr[i][1]:
                flag[i] = 1
                count += 1
        else:
            if arr[i][0] - arr[i - 1][0] > arr[i][1]:
                flag[i] = -1
                count += 1
            elif arr[i + 1][0] - arr[i][0] > arr[i][1]:
                flag[i] = 1
                count += 1
    print(count)
