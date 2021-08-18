def sum_fracts(lst):
    print(lst)
    if lst == []:
        return None
    ll = len(lst)
    n, cd, md = 2, 1, min(lst[i][1] for i in range(ll))
    while n <= md:
        if all(lst[i][1] % n == 0 for i in range(ll)):
            cd = n
        n += 1
    print(('max common divider: {}'.format(cd)))

    dd = cd
    for i in range(ll):
        dd = dd * (lst[i][1] // cd)

    nn = sum(lst[i][0] * (dd // lst[i][1]) for i in range(ll))

    i, primes = 0, [2, 3, 5, 7, 11, 13, 17]
    while i < len(primes):
        n = primes[i]
        if nn % n == 0 and dd % n == 0:
            nn = nn // n
            dd = dd // n
        else:
            i += 1
    if dd == 1:
        return nn
    else:
        return [nn, dd]
