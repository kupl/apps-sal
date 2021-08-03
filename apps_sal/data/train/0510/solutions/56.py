#!python3

import sys


def iim(): return map(int, input().rstrip().split())


def resolve():
    N = int(input())
    S = list(input())
    Q = int(input())

    c0 = ord('a')
    smap = [1 << (i - c0) for i in range(c0, ord('z') + 1)]

    T = [0] * N + [smap[ord(S[i]) - c0] for i in range(N)]

    for i in range(N - 1, 0, -1):
        i2 = i << 1
        T[i] = T[i2] | T[i2 | 1]

    ans = []
    # print(T)
    for cmd, i, j in zip(*[iter(sys.stdin.read().split())] * 3):
        i = int(i) - 1
        if cmd == "1":
            if S[i] == j:
                continue

            S[i] = j
            i0 = N + i
            T[i0] = smap[ord(j) - c0]
            while i0 > 1:
                i0 = i0 >> 1
                T[i0] = T[i0 + i0] | T[i0 - ~i0]
        elif cmd == "2":
            i += N
            j = int(j) + N

            d1 = 0
            while i < j:
                if i & 1:
                    d1 |= T[i]
                    i += 1
                if j & 1:
                    j -= 1
                    d1 |= T[j]

                i >>= 1
                j >>= 1

            ans.append(bin(d1).count('1'))

    print(*ans, sep="\n")


def __starting_point():
    resolve()


__starting_point()
