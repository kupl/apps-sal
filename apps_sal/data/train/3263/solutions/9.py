def solve(a):
    return (lambda s: '%02d:%02d' % divmod(max(((b - a - 1) % 1440 for (a, b) in zip(s, s[1:] + s))), 60))(sorted({60 * int(t[:2]) + int(t[3:]) for t in a}))
