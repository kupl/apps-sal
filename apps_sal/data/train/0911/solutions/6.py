import bisect as bi

temp_g = [0, 1, 2]
temp_s = [0, 1, 9]
temp_p = [0, 1, 3]
max_mod = (10 ** 9 + 7)


def find_gn(n):
    return (1 + temp_g[n - temp_g[temp_g[n - 1]]])


def find_sn(n, gn):
    return (temp_s[n - 1] + gn * n * n) % max_mod


def find_pn(n, gn):
    return (temp_p[n - 1] + gn)


def bisection(x):
    n = bi.bisect_right(temp_p, x)
    return (temp_s[n - 1] + (x - temp_p[n - 1]) * n * n) % max_mod


lr, max_ = [], 100

for _ in range(int(input())):
    l, r = list(map(int, input().split()))
    lr.append((l, r))
    max_ = max(max_, r + 1)

for n in range(3, 2 * (10 ** 8), 1):
    gn = find_gn(n)
    sn, pn = find_sn(n, gn), find_pn(n, gn)
    temp_g.append(gn)
    temp_p.append(pn)
    temp_s.append(sn)
    if (pn > max_):
        break

for pair in lr:
    print(bisection(pair[1]) - bisection(pair[0] - 1) % max_mod)
