# -*- coding: utf-8 -*-
import sys
# sys.setrecursionlimit(10**6)
# buff_readline = sys.stdin.buffer.readline
buff_readline = sys.stdin.readline
readline = sys.stdin.readline

INF = 2**62-1


def read_int():
    return int(buff_readline())


def read_int_n():
    return list(map(int, buff_readline().split()))


# @mt
def slv(N, M, A, B):
    if N * A != M*B:
        print('NO')
        return

    print('YES')
    mat = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(A):
            mat[i][(i*A+j)%M] = 1

    for r in mat:
        print(''.join(map(str, r)))



def main():
    T = read_int()
    for _ in range(T):
        N, M, A, B = read_int_n()
        slv(N, M, A, B)


def __starting_point():
    main()

__starting_point()
