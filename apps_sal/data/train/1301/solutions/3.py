import math
from collections import defaultdict as dd
from sys import stdin, stdout
input = stdin.readline
def geti(): return list(map(int, input().strip().split()))
def getl(): return list(map(int, input().strip().split()))
def gets(): return input()
def geta(): return int(input())
def print_s(s): stdout.write(s + '\n')


def solve():
    for _ in range(geta()):
        n = geta()
        a = sorted(list(str(n)), reverse=True)
        print(int(''.join(a)))


def __starting_point():
    solve()


__starting_point()
