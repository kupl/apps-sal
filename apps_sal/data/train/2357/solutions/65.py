
import sys


def read_str(): return sys.stdin.readline().strip()
def read_int(): return int(sys.stdin.readline().strip())
def read_ints(): return list(map(int, sys.stdin.readline().strip().split()))
def read_str_split(): return list(sys.stdin.readline().strip())
def read_int_list(): return list(map(int, sys.stdin.readline().strip().split()))


def nCr(n, r, MOD):
    a, b = 1, 1
    for i in range(r):
        a = a * (n - i) % MOD
        b = b * (i + 1) % MOD
    return a * pow(b, MOD - 2, MOD) % MOD


def Main():
    N, M = read_ints()
    A = read_int_list()
    print((nCr(N + M, N + sum(A), 10**9 + 7)))


def __starting_point():
    Main()


__starting_point()
