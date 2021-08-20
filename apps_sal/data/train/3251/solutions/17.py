def primeFactors(n):
    a = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            a.append(i)
            n //= i
        i += 1
    if n != 1:
        a.append(n)
    s = [i for i in set(a)]
    s.sort()
    return ''.join(('({})'.format(i) if a.count(i) == 1 else '({}**{})'.format(i, a.count(i)) for i in s))
