def primeFactors(x):
    primes = {}
    prime_int = 2
    y = x
    while prime_int < x + 1:
        while x % prime_int == 0:
            if prime_int not in primes:
                primes[prime_int] = 1
            else:
                primes[prime_int] += 1
            x //= prime_int
        prime_int += 1
    phrase = ''
    for digit, count in primes.items():
        if count == 1:
            phrase += f'({digit})'
            continue
        phrase += f'({digit}**{count})'
    print(phrase)
    return phrase
