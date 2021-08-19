import sys
import collections
input = sys.stdin.readline


def main():
    S = input().strip()
    T = input().strip()
    Q = int(input())
    ABCD = [[int(x) for x in input().split()] for _ in range(Q)]
    TAruiseki = [0] * (len(S) + 1)
    TBruiseki = [0] * (len(S) + 1)
    SAruiseki = [0] * (len(S) + 1)
    SBruiseki = [0] * (len(S) + 1)
    for (i, s) in enumerate(S):
        if s == 'A':
            SAruiseki[i + 1] += 1
            SAruiseki[i + 1] += SAruiseki[i]
            SBruiseki[i + 1] += SBruiseki[i]
        else:
            SBruiseki[i + 1] += 1
            SBruiseki[i + 1] += SBruiseki[i]
            SAruiseki[i + 1] += SAruiseki[i]
    for (i, t) in enumerate(T):
        if t == 'A':
            TAruiseki[i + 1] += 1
            TAruiseki[i + 1] += TAruiseki[i]
            TBruiseki[i + 1] += TBruiseki[i]
        else:
            TBruiseki[i + 1] += 1
            TBruiseki[i + 1] += TBruiseki[i]
            TAruiseki[i + 1] += TAruiseki[i]
    for (a, b, c, d) in ABCD:
        sacnt = SAruiseki[b] - SAruiseki[a - 1]
        sbcnt = SBruiseki[b] - SBruiseki[a - 1]
        tacnt = TAruiseki[d] - TAruiseki[c - 1]
        tbcnt = TBruiseki[d] - TBruiseki[c - 1]
        if (sacnt - tacnt) % 3 == (sbcnt - tbcnt) % 3:
            print('YES')
        else:
            print('NO')


def __starting_point():
    main()


__starting_point()
