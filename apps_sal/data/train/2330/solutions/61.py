#from collections import deque
#from heapq import heapify, heappop, heappush
#from bisect import insort, bisect_left
#import sys
# sys.setrecursionlimit(10**9)
#from math import gcd
#from decimal import Decimal
#mod = 1000000007
#mod = 998244353
#N = int(input())
#N, K = map(int, input().split())
S = input()
eda = []
flag = False
N = len(S)
if S[-1] == '1':
    flag = True
if S[0] == '0':
    flag = True
if S[-2] == '0':
    flag = True
for k in range((N - 1) // 2):
    if S[k] != S[-k - 2]:
        flag = True
    if S[k] == '1':
        eda.append(k + 1)
if N % 2 == 0:
    if S[N // 2 - 1] == '1':
        eda.append(N // 2)
if flag:
    print((-1))
    return
ans = []
eda.reverse()
before = eda.pop()
while eda:
    after = eda.pop()
    for k in range(before, after):
        ans.append((k, after))
    before = after
ans.append((before, before + 1))
for k in range(before + 2, N + 1):
    ans.append((before + 1, k))
while ans:
    item = ans.pop()
    print((item[0], item[1]))
#ans = 0
# for k in range(N):
# print(ans)
# print('Yes')
# print('No')
