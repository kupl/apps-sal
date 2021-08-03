def primeFactors(n):
    def is_prime(number):
        if number == 1:
            return False
        for num in range(3, (int)(number**.5) + 1, 2):
            if number % num == 0:
                return False
        return True
    primes_prelimenary = []
    while n > 1:
        if is_prime(n):
            primes_prelimenary.append(n)
            n = 1
            continue
        while n % 2 == 0:
            primes_prelimenary.append(2)
            n = n / 2
        for num in range(3, (int)(n**.5) + 1, 2):
            if n % num == 0 and is_prime(num):
                while n % num == 0:
                    primes_prelimenary.append(num)
                    n = n / num
    return ''.join(f'({(int)(factor)}**{primes_prelimenary.count(factor)})' for factor in sorted(set(primes_prelimenary))).replace('**1', '')
