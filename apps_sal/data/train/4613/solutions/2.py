def add(a, b):
    (out, ap, bp, r) = ('', list(a.lstrip('0')), list(b.lstrip('0')), 0)
    while len(ap) > 0 or len(bp) > 0 or r > 0:
        (ac, bc) = (ap.pop() if len(ap) > 0 else None, bp.pop() if len(bp) else None)
        total = r + (ac == '1') + (bc == '1')
        out = ('1' if total % 2 else '0') + out
        r = 0 if total < 2 else 1
    return out or '0'
