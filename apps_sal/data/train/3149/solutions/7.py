def roof_fix(f, r):
    for i in range(len(r)):
        if r[i] in "/\\" and f[i] != ' ':
            return False
    return True
