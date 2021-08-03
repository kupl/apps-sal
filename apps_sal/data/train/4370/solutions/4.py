def indices(n, d):
    result = []
    temp = []

    def tt(n, d, temp):
        if d == 1:
            result.extend([temp + [n]])
            return 0
        for i in range(0, n + 1):
            aa = temp + [i]
            tt(n - i, d - 1, aa)
    tt(d, n, temp)
    return result
