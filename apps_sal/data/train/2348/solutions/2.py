import sys
import bisect


def solve():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    n = int(input().rstrip('\n'))
    x = [v for v in list(map(int, input().rstrip('\n').split()))]
    l = int(input().rstrip('\n'))
    q = int(input().rstrip('\n'))
    ln = 64
    lsf = [[-1] * ln for _ in range(n)]
    lsb = [[-1] * ln for _ in range(n)]
    for i in range(n - 1):
        lsf[i][0] = bisect.bisect_right(x, x[i] + l) - 1
        lsb[-i - 1][0] = bisect.bisect_left(x, x[-i - 1] - l)
    for j in range(1, ln):
        for i in range(n):
            if lsf[i][j - 1] != -1:
                lsf[i][j] = lsf[lsf[i][j - 1]][j - 1]
            if lsb[i][j - 1] != -1:
                lsb[i][j] = lsb[lsb[i][j - 1]][j - 1]

    for i in range(q):
        a, b = list(map(int, input().rstrip('\n').split()))
        a, b = a - 1, b - 1
        cnt = 0
        if a < b:
            for j in range(b.bit_length(), -1, -1):
                if lsf[a][j] != -1:
                    if lsf[a][j] <= b:
                        cnt += 2 ** j
                        a = lsf[a][j]
        else:
            for j in range(a.bit_length(), -1, -1):
                if lsb[a][j] != -1:
                    if lsb[a][j] >= b:
                        cnt += 2 ** j
                        a = lsb[a][j]
        cnt += 0 if a == b else 1
        print(cnt)


def __starting_point():
    solve()


__starting_point()
