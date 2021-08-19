def trailing_zeros(num, base):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    plist = []
    pow = []
    b = base
    for p in primes:
        if b % p == 0:
            plist.append(p)
            ctr = 0
            while b % p == 0:
                b //= p
                ctr += 1
            pow.append(ctr)
    i = 101
    iinc = 2
    while b > 1:
        if b % i == 0:
            if isprime(i):
                plist.append(i)
                ctr = 0
                while b % i == 0:
                    b = b // i
                    ctr += 1
                pow.append(ctr)
        i += iinc
        iinc = 6 - iinc
        if i * i > b:
            i = b
    if len(plist) == 0:
        return 0
    plist.sort()
    accmax = 1e309
    while len(plist) > 0:
        acc = 0
        a = plist[-1]
        aa = pow[-1]
        n = num
        while n != 0:
            n = n // a
            acc += n
        acc = acc // aa
        plist.pop()
        pow.pop()
        if acc < accmax:
            accmax = acc
    return accmax


def isprime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    a = 5
    ainc = 2
    while a * a <= n:
        if n % a == 0:
            return False
        a += ainc
        ainc = 6 - ainc
    return True
