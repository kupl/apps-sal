l, m = 10082, 104
a, d, s, t = 0, 1, {}, [0]
for _ in range(l + m - 1):
    s[a] = 1 - s.get(a, 0)
    v = (-1) ** -~s[a]
    d *= 1j * v
    a += d
    t.append(t[-1] + v)


def langtons_ant(n):
    if n < l:
        return t[n]
    q, r = divmod(n - l, m)
    return 12 * q + t[l + r]
