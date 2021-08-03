from functools import reduce


def colorful(n):
    p = list(get_sub_mul(n))
    return len(p) == len(set(p))


def get_sub_mul(n):
    s = [int(d) for d in str(n)]
    l = len(s)
    for k in range(1, l + 1):
        for i in range(l - k + 1):
            yield reduce(int.__mul__, s[i:i + k])
