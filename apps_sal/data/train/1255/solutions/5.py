import math
import sys
from collections import Counter, defaultdict, deque
from sys import stdin, stdout
input = stdin.readline
def lili(): return list(map(int, sys.stdin.readlines()))
def li(): return list(map(int, input().split()))
def I(): return int(input())
def S(): return input().strip()


mod = 1000000007

for i in range(I()):
    s, n = list(map(str, input().split()))
    n = int(n)
    p = "abcdefghijklmnopqrstuvwxyz"
    d = Counter(s)
    ans = ""
    for i in p:
        if(len(ans) == len(s)):
            break
        if(i not in d):
            ans += i
        else:
            if(n):
                ans += i
                n -= 1
    if(len(ans) == len(s)):
        print(ans)
    else:
        print("NOPE")
