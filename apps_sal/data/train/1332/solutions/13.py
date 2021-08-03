
def read_mapped(func=lambda x: x):
    return list(map(func, input().split(" ")))


def read_array(N, func):
    l = []
    for i in range(N):
        l.append(func(input()))
    return l


def read_int():
    return int(input())


def read_str():
    return input()


def read_float():
    return float(input())


T = read_int()


def solve(m, n, s):
    if m == n:
        return s

    if m < n:
        m, n = n, m
    if m % 2 == 0:
        return solve(m / 2, n, s + 1)
    else:
        return solve((m - 1) / 2, n, s + 1)


for case in range(T):
    i, j = read_mapped(int)
    si = min(i, j)
    sj = max(i, j)
    print(solve(sj, si, 0))
