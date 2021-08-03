# Target - Expert on CF
# Be Humblefool

import sys

inf = float("inf")
# sys.setrecursionlimit(1000000)

# abc='abcdefghijklmnopqrstuvwxyz'
# abd={'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
mod, MOD = 1000000007, 998244353
# words = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'quarter',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',21:'twenty one',22:'twenty two',23:'twenty three',24:'twenty four',25:'twenty five',26:'twenty six',27:'twenty seven',28:'twenty eight',29:'twenty nine',30:'half'}
# vow=['a','e','i','o','u']
# dx,dy=[0,1,0,-1],[1,0,-1,0]

# import random
# from collections import deque, Counter, OrderedDict,defaultdict
# from heapq import nsmallest, nlargest, heapify,heappop ,heappush, heapreplace
# from math import ceil,floor,log,sqrt,factorial,pi,gcd
# from bisect import bisect,bisect_left,bisect_right,insort,insort_left,insort_right


def get_array(): return list(map(int, sys.stdin.readline().strip().split()))
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def input(): return sys.stdin.readline().strip()


Arr = [0]
dp = [0]
prev_sum = 0
prev_length = 1
n = int(input())
while n:
    arr = get_array()
    if len(arr) == 2:
        number = arr[1]
        Arr.append(number)
        dp.append(0)
        ans = (prev_sum + number) / (prev_length + 1)
        print(ans)
        prev_length += 1
        prev_sum += number
    elif len(arr) == 3:
        a, x = arr[1], arr[2]
        dp[a - 1] += x
        ans = (prev_sum + a * x) / (prev_length)
        print(ans)
        prev_sum += a * x
    else:
        ans = (prev_sum - (Arr[-1] + dp[-1])) / (prev_length - 1)
        print(ans)
        prev_sum -= (Arr[-1] + dp[-1])
        prev_length -= 1
        dp[-2] += dp[-1]
        Arr.pop()
        dp.pop()
    n -= 1
