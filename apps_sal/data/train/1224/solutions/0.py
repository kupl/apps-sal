import fractions
import sys
f = sys.stdin
if len(sys.argv) > 1:
    f = open(sys.argv[1], 'rt')
sum_cache = {}


def sum_func(x):
    if x < 10:
        return x
    r = sum_cache.get(x)
    if r is not None:
        return r
    xx = 0
    while x > 0:
        xx += x % 10
        x /= 10
    r = sum_func(xx)
    sum_cache[x] = r
    return r


def test():
    for n in range(1):
        print(n, sum_func(n))
    print(sum_func(int(10 ** 18 - 1)))


cycle_table = [[9, [1, 1, 1, 1, 1, 1, 1, 1, 1]], [9, [1, 1, 1, 1, 1, 1, 1, 1, 1]], [3, [1, 0, 0, 1, 0, 0, 1, 0, 0]], [9, [1, 1, 1, 1, 1, 1, 1, 1, 1]], [9, [1, 1, 1, 1, 1, 1, 1, 1, 1]], [3, [1, 0, 0, 1, 0, 0, 1, 0, 0]], [9, [1, 1, 1, 1, 1, 1, 1, 1, 1]], [9, [1, 1, 1, 1, 1, 1, 1, 1, 1]], [1, [1, 0, 0, 0, 0, 0, 0, 0, 0]]]
NUMBER = 9


def calc(A_1, D, L, R):
    A_L = A_1 + D * (L - 1)
    A_L_kfunc = sum_func(A_L)
    D_kfunc = sum_func(D)
    n = R - L + 1
    if D == 0:
        return n * A_L_kfunc
    cycle_len = cycle_table[D_kfunc - 1][0]
    cycle_markers = list(cycle_table[D_kfunc - 1][1])
    whole_part = n // cycle_len
    remainder = n % cycle_len
    counts = [whole_part * x for x in cycle_markers]
    pos = 0
    for i in range(remainder):
        counts[pos] += 1
        pos = (pos + D_kfunc) % NUMBER
    r = 0
    for (i, x) in enumerate(counts):
        value = (A_L_kfunc - 1 + i) % NUMBER + 1
        r += value * x
    return r


def calc_dumb(A_1, D, L, R):
    a = A_1 + D * (L - 1)
    n = R - L + 1
    r = 0
    for i in range(n):
        value = sum_func(a)
        r += value
        a += D
    return r


def test1():
    a1 = 1
    L = 1
    R = 1000
    for d in range(100):
        r1 = calc_dumb(a1, d, L, R)
        r2 = calc(a1, d, L, R)
        if r1 != r2:
            print(a1, d, L, R, ':', r1, r2)


def test2():
    a1 = 1
    d = 9
    L = 1
    R = 9
    r1 = calc_dumb(a1, d, L, R)
    r2 = calc(a1, d, L, R)
    print(r1, r2)


T = int(f.readline().strip())
for case_id in range(1, T + 1):
    (A_1, D, L, R) = list(map(int, f.readline().strip().split()))
    r = calc(A_1, D, L, R)
    print(r)
