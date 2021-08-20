import sys


def Fact(n):
    s = 1
    for i in range(2, n + 1):
        s *= i
    return s


N = int(sys.stdin.readline())
for i in range(N):
    T = int(sys.stdin.readline())
    print(Fact(T))
