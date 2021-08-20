def primeFactors(n):
    r = ''
    pf = 1
    while n > 1:
        pf += 1
        num = 0
        while n % pf == 0:
            n /= pf
            num += 1
        if num > 0:
            r += '(' + str(pf) + '**' + str(num) + ')'
    r = r.replace('**1', '')
    return r
