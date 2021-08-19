import sys
import bisect
input = sys.stdin.readline
N = int(input())
x = list(map(int, input().split()))
L = int(input())
doubling = [[-1 for i in range(N)] for j in range(20)]
for i in range(N):
    npos = x[i] + L
    index = bisect.bisect_right(x, npos)
    doubling[0][i] = index - 1
for i in range(1, 20):
    for j in range(N):
        doubling[i][j] = doubling[i - 1][doubling[i - 1][j]]
forward = [[-1 for i in range(N)] for j in range(20)]
for i in range(N):
    forward[0][i] = i
for i in range(1, 20):
    for j in range(N):
        forward[i][j] = doubling[i - 1][forward[i - 1][j]]
for _ in range(int(input())):
    (a, b) = map(int, input().split())
    a -= 1
    b -= 1
    if a > b:
        (a, b) = (b, a)
    res = 0
    for i in range(19, -1, -1):
        if b > forward[i][a]:
            a = doubling[i][a]
            res += 2 ** i
    print(res)
