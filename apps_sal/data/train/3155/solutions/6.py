def fit_in(a, b, m, n):
    if a + b <= m:
        if max(a, b) <= n:
            return True
        else:
            return False
    elif max(a, b) <= m:
        if a + b <= n:
            return True
        else:
            return False
    else:
        return False
