def primeFactors(n):
    result = ''
    factor = 2
    while 1:
        count = 0
        while n % factor == 0:
            count += 1
            n = n / factor
        if count == 1 and count != 0:
            result = result + '(%s)' % factor
        elif count != 0:
            result = result + '({}**{})'.format(factor, count)
        else:
            factor += 1
            continue
        factor += 1
        if n == 1:
            break
    return result
