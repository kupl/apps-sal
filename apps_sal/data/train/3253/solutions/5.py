def womens_age(n):
    a = 2
    L1 = [0, 1]
    for i in L1:
        x = int((n - L1[i]) / a)
        if (n % x) == L1[i]:
            base = x
            result = "%d%d" % (a , L1[i])
    return str(n) + "? That's just " + str(result) + ", in base " + str(base) + "!"
