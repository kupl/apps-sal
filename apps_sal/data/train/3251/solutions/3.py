def primeFactors(n):
    result = ''
    fac = 2
    while fac <= n:
        count = 0
        while n % fac == 0:
            n /= fac
            count += 1
        if count:
            result += '(%d%s)' % (fac, '**%d' % count if count > 1 else '')
        fac += 1
    return result
