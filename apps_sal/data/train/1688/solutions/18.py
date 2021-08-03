from sys import stdin, stdout
from math import gcd
def st(): return list(stdin.readline().strip())


def li(): return list(map(int, stdin.readline().split()))
def mp(): return map(int, stdin.readline().split())
def inp(): return int(stdin.readline())
def pr(n): return stdout.write(str(n) + "\n")


mod = 1000000007


def solve():
    n = inp()
    l = li()
    pr(''.join(list(map(str, l))))


for _ in range(inp()):
    solve()
