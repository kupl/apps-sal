import sys


def input():
    return sys.stdin.readline().rstrip('\r\n')


for _ in range(int(input())):
    k = int(input())
    res = []
    for i in range(k):
        res.append(i + 1)
    for j in range(k - 1, 0, -1):
        res.append(j)
    s = 0
    for i in res:
        s = s + i * i * i
    print(s)
