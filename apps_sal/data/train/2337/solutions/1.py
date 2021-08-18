import sys
import os
3


def main():
    T = read_int()
    for _ in range(T):
        N = read_int()
        P = read_ints()
        print(*solve(N, P))


def solve(N, P):
    C = []
    i = 0
    while i < N:
        j = i + 1
        while j < N and P[j] == P[i]:
            j += 1
        C.append(j - i)
        i = j

    if N < 10 or len(C) < 3:
        return 0, 0, 0

    half = N // 2
    g = C[0]
    s = 0
    i = 1
    while i < len(C) and g >= s:
        s += C[i]
        i += 1
    b = 0
    while i < len(C) and g >= b:
        b += C[i]
        i += 1
    if s == 0 or b == 0 or g >= s or g >= b or g + s + b > half:
        return 0, 0, 0
    while i < len(C):
        if g + s + b + C[i] > half:
            break
        b += C[i]
        i += 1
    return g, s, b


DEBUG = 'DEBUG' in os.environ


def inp():
    return sys.stdin.readline().rstrip()


def read_int():
    return int(inp())


def read_ints():
    return [int(e) for e in inp().split()]


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


def __starting_point():
    main()


__starting_point()
