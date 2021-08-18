
import sys


def iim(): return map(int, input().rstrip().split())


def popcnt2(n):
    a = (
        0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4,
        1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
        1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
        2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
        1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
        2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
        2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
        3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
        1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
        2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
        2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
        3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
        2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
        3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
        3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
        4, 5, 5, 6, 5, 6, 6, 7, 5, 6, 6, 7, 6, 7, 7, 8,
    )
    ans = 0
    while n:
        ans += a[n & 0xff]
        n >>= 8
    return ans


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
    for cmd, i, j in (line.split() for line in sys.stdin.readlines()):
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

            ans.append(popcnt2(d1))

    print(*ans, sep="\n")


def __starting_point():
    resolve()


__starting_point()
