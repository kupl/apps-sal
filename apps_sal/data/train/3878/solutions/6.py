def kangaroo(k1, r1, k2, r2):
    dif = r1 - r2
    try:
        a, b = (k1 - k2), (r1 - r2)
        return a % b == 0 and (a < 0) != (b < 0)
    except Exception:
        return False
