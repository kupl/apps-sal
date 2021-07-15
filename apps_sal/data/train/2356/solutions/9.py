# -*- coding: utf-8 -*-

import sys
sys.setrecursionlimit(10**6)
# readline = sys.stdin.buffer.readline
readline = sys.stdin.readline

INF = 1 << 60


def read_int():
    return int(readline())


def read_int_n():
    return list(map(int, readline().split()))


def read_float():
    return float(readline())


def read_float_n():
    return list(map(float, readline().split()))


def read_str():
    return readline().strip()


def read_str_n():
    return readline().strip().split()


def ep(*args):
    print(*args, file=sys.stderr)


def mt(f):
    import time

    def wrap(*args, **kwargs):
        s = time.perf_counter()
        ret = f(*args, **kwargs)
        e = time.perf_counter()

        ep(e - s, 'sec')
        return ret

    return wrap


def gen_2d(n, m, fill=0):
    return [[fill] * m for _ in range(n)]


@mt
def slv(N, K):
    memo = gen_2d(N+1, 2*N+1)
    memo[0][0] = 1
    M = 998244353
    for n in range(1, N+1):
        for k in range(n, 0, -1):
            x = memo[n-1][k-1]
            x += memo[n][k*2]
            x %= M
            memo[n][k] = x
    return memo[N][K]


def main():
    N, K = read_int_n()
    print(slv(N, K))


def __starting_point():
    main()

__starting_point()
