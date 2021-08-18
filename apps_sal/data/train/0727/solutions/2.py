import sys

T = int(sys.stdin.readline())


def calc_min_len(l, r):
    if l + 1 == r:
        return 0
    if l >= r:
        return 0

    m = (l + r) // 2
    return m - l + r - m + calc_min_len(l, m) + calc_min_len(m, r)


def calc_max_len(n):
    return sum(range(2, N + 2))


for t in range(T):
    N, M = list(map(int, sys.stdin.readline().split()))

    min_len = calc_min_len(1, N + 2)
    max_len = calc_max_len(N)

    if M < min_len:
        print(-1)
    elif M > max_len:
        print(M - max_len)
    else:
        print(0)
