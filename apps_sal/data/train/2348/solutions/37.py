from bisect import bisect_right
import sys
input = sys.stdin.readline

N = int(input())
x = list(map(int, input().split()))
L = int(input())
log = 1
while 1 << log < N:
    log += 1
doubling = [[0] * (log + 1) for _ in range(N)]
for i in range(N):
    j = bisect_right(x, x[i] + L) - 1
    doubling[i][0] = j
for l in range(1, log + 1):
    for i in range(N):
        doubling[i][l] = doubling[doubling[i][l - 1]][l - 1]
Q = int(input())
for _ in range(Q):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    if a > b:
        a, b = b, a
    ans = 0
    for l in range(log, -1, -1):
        if doubling[a][l] < b:
            ans += 1 << l
            a = doubling[a][l]
    print((ans + 1))
