def bouncy_ratio(target):
    bouncy = 0.0
    n = 100

    while bouncy / n < target:
        n += 1
        s = list(str(n))
        s_ = sorted(s)
        if s != s_ and s != s_[::-1]:
            bouncy += 1

    return n
