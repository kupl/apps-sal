def roof_fix(f, r):
    for (u, y) in zip(f, r):
        if u.isalpha() and y in '/\\':
            return False
    return True
