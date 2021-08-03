import sys
import bisect as bi
import math
from collections import defaultdict as dd
input = sys.stdin.readline
# sys.setrecursionlimit(10**7)


def cin():
    return list(map(int, sin().split()))


def ain():
    return list(map(int, sin().split()))


def sin():
    return input()


def inin():
    return int(input())


for _ in range(inin()):
    s = sin().strip()
    q = inin()
    a = ain()
    n = len(s)
    store = [0] * n
    store1 = [-1] * n
    f = 0
    d = dd(int)  # input wgera
    store[0] = 1 if s[0] == '(' else -1
    d[store[0]] = 1
    for i in range(1, n):
        if(s[i] == '('):
            store[i] = store[i - 1] + 1
            d[store[i]] = i + 1
        else:
            store[i] = store[i - 1] - 1
            if(d[store[i - 1]]):
                store1[d[store[i - 1]] - 1] = i + 1
    post = [-1] * n
    if(n == 1 or (n == 2 and s != "()")):
        f = 1   # corner case
    for i in range(n - 2, -1, -1):
        if(s[i] == '('):  # dekhna h ki agla agr ( h toh -1 hi rhega wrna wo jo stored tha uppr
            if(store1[i] != -1):
                post[i] = store1[i]  # wo iska ans ho jayega
        else:
            post[i] = post[i + 1]  # jo iske agle ka answer hoga wahi iska hoga
    for i in a:
        if(f):
            print(-1)  # cond ki jaroorat nhi thi pr tasalli (>_<)
        else:
            print(post[i - 1])  # wrna uska ans print kra do


# n=m=0
# s=''
# t=''
# dp=[]
# def solve(inds,indt,k,cont):
# ans=-999999999999999
# print(dp)
# if(k<0):return 0
# elif(inds>=n and indt>=m):return 0
# elif(dp[inds][indt][k][cont]!=-1):return dp[inds][indt][k][cont]
# else:
# if(indt<m):ans=max(ans,solve(inds,indt+1,k,0))
# if(inds<n):ans=max(ans,solve(inds+1,indt,k,0))
# if(s[inds]==t[indt]):
# ans=max(ans,solve(inds+1,indt+1,k-1,1)+1)
# if(cont):ans=max(ans,solve(inds+1,indt+1,k,1)+1)
# dp[inds][indt][k][cont]=ans
# return ans

# n,m,k=cin()
# s=sin().strip()
# t=sin().strip()
##    dp=[[[[-1]*2 for i in range(k)] for i in range(m+1)] for i in range(n+1)]
# c=0
# for i in dp:
# for j in i:
# for l in j:
# c+=1
# print(l,c)
# print(solve(0,0,k,0))
