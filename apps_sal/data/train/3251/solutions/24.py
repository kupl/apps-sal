def primeFactors(n):
    res = ''
    fac = 2
    while fac <= n:
        count = 0
        while n % fac == 0:
            count += 1
            n = n / fac
        if count > 0:
            res += '(' + str(fac)
            res += '**' + str(count) if count > 1 else ''
            res += ')'
        fac += 1
    return res
