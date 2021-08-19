from bisect import bisect
from operator import mul
from functools import partial, reduce
import sys
sys.setrecursionlimit(10 ** 7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
prod = partial(reduce, mul)


def LI():
    return [int(x) for x in sys.stdin.readline().split()]


def LI_():
    return [int(x) - 1 for x in sys.stdin.readline().split()]


def LF():
    return [float(x) for x in sys.stdin.readline().split()]


def LS():
    return sys.stdin.readline().split()


def II():
    return int(sys.stdin.readline())


def SI():
    return input()


def main():
    N = II()
    X = LI()
    X.append(INF)
    L = II()
    Q = II()
    AB = []
    for _ in range(Q):
        AB.append(LI_())
    Unreachs = [[] for _ in range(N)]
    for (i, x) in enumerate(X[:-1]):
        u = bisect(X, x + L)
        Unreachs[i].append(u)
    updated = True
    while updated:
        updated = False
        for i in range(N):
            u = Unreachs[Unreachs[i][-1] - 1][-1]
            updated = updated or u != Unreachs[i][-1]
            Unreachs[i].append(u)
    for (a, b) in AB:
        if a > b:
            (a, b) = (b, a)
        ans = 0
        while True:
            k = bisect(Unreachs[a], b) - 1
            if k < 0:
                ans += 1
                break
            ans += 2 ** k
            a = Unreachs[a][k] - 1
        print(ans)
    return 0


main()
