def is_exact(n, sn, p):
    return n > 99 and (all((d == '0' for d in sn[1:])) or all((d == sn[0] for d in sn)) or sn in '1234567890' or (sn in '9876543210') or (sn == sn[::-1]) or (n in p))


def is_interesting(n, p):
    return next([_f for _f in (1 + (v == n) if is_exact(v, str(v), p) else 0 for v in range(n, n + 3)) if _f], 0)
