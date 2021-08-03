def sub(a, s):
    pa = 0
    ps = 0
    while pa < len(a) and ps < len(s):
        if a[pa] == s[ps]:
            ps += 1
            pa += 1
        else:
            pa += 1

    return ps == len(s)


def subword(t, ord_ar, n):
    t_copy = []
    for i in range(len(ord_ar)):
        if ord_ar[i] >= n:
            t_copy.append(t[i])
    return t_copy


def check(t, p, ord_ar, n):
    s = subword(t, ord_ar, n)
    return sub(s, p)


def bin_s(l, r, f):
    while r > l + 1:
        m = (r + l) // 2
        if f(m):
            l = m
        else:
            r = m
    return l


def main():
    t = input().strip()
    p = input().strip()
    ord_ar = [0] * len(t)

    seq = list(map(int, input().strip().split()))
    for i, x in enumerate(seq):
        ord_ar[x - 1] = i

    ans = bin_s(0, len(t), lambda n: check(t, p, ord_ar, n))
    print(ans)


main()
