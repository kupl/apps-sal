def primeFactors(n):
    div = 2
    k = 0
    s = ''
    while div < n:
        while n % div != 0:
            div += 1
        while n % div == 0:
            n = n // div
            k += 1
        s += '({}{})'.format(str(div), '**' + str(k) if k > 1 else '')
        k = 0
    return s
