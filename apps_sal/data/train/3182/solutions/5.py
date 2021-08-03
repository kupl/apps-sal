def LDTA(n):
    if set(str(n)) == set(str(n ** 2)):
        return
    res, i = [], 0
    while True:
        i += 1
        for digit in str(n ** i):
            if digit not in res:
                res.append(digit)
            if len(res) >= 10:
                return int(res[-1])
