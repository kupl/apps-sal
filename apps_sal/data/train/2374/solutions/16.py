import heapq
import math
import sys
input = sys.stdin.readline


def li():
    return [int(i) for i in input().rstrip('\n').split()]


def value():
    return int(input())


def typ(a):
    if a < 3:
        return 1
    return 2


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().rstrip('\n')))
    b = list(map(int, input().rstrip('\n')))
    for i in range(n):
        a[i] = [a[i], b[i]]
    ans = 1
    currline = 0
    for i in range(n):
        if typ(a[i][currline]) == 2:
            currline = not currline
            if typ(a[i][currline]) == 1:
                ans = 0
                break
    if currline == 0:
        ans = 0
    if ans:
        print('YES')
    else:
        print('NO')
