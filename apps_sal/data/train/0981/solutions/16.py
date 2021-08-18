import sys
readin = sys.stdin.readline


def readnums():
    return list(map(int, readin().split()))


T = eval(input())
for i1 in range(T):
    N = eval(input())
    l = readnums()
    l.sort()
    m = 1000000000
    for i2 in range(len(l) - 1):
        if l[i2 + 1] - l[i2] < m:
            m = l[i2 + 1] - l[i2]
    print(m)
