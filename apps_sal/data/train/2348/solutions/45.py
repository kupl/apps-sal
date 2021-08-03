import sys
import bisect

input = sys.stdin.readline

N = int(input())
x = list(map(int, input().split()))
L = int(input())

doubling = [[-1 for i in range(N)] for j in range(20)]
backdoubling = [[-1 for i in range(N)] for j in range(20)]

for i in range(N):
    npos = x[i] + L
    index = bisect.bisect_right(x, npos)
    doubling[0][i] = index - 1

for i in range(1, 20):
    for j in range(N):
        doubling[i][j] = doubling[i - 1][doubling[i - 1][j]]

for i in range(N):
    npos = x[i] - L
    index = bisect.bisect_left(x, npos)
    backdoubling[0][i] = index

for i in range(1, 20):
    for j in range(N):
        backdoubling[i][j] = backdoubling[i - 1][backdoubling[i - 1][j]]


def forward(num, start):
    for i in range(20):
        if num >> i & 1 == 1:
            start = doubling[i][start]
    return start


def back(num, start):
    for i in range(20):
        if num >> i & 1 == 1:
            start = backdoubling[i][start]
    return start


for _ in range(int(input())):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if b >= a:
        s = 0
        e = N
        while e - s > 1:
            test = (e + s) // 2
            if forward(test, a) >= b:
                e = test
            else:
                s = test
        if forward(s, a) >= b:
            print(s)
        else:
            print(e)
    else:
        s = 0
        e = N
        while e - s > 1:
            test = (e + s) // 2
            if b >= back(test, a):
                e = test
            else:
                s = test
        if b >= back(s, a):
            print(s)
        else:
            print(e)
