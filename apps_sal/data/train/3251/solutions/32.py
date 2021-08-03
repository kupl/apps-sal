def primeFactors(n):
    comp = []
    i = 1
    o = 0
    while n != 1:
        i = i + 1
        if n % i == 0:
            o = o + 1
            while n % i == 0:
                n = n / i
                comp.append(i)
    if o == 0:
        return '(' + str(n) + ')'
    g = ['(' + str(x) + '**' + str(comp.count(x)) + ')' if comp.count(x) > 1 else '(' + str(x) + ')' for x in sorted(list(set(comp)))]
    return ''.join(g)
