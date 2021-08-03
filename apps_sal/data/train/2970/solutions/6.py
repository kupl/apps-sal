product_numbers = {
    1: [4, 6, 9, 10, 14, 15, 21, 22, 25, 26, 33, 34, 35, 38, 39, 46, 49, 51, 55, 57, 58, 62, 65, 69, 74, 77, 82, 85, 86, 87, 91, 93, 94, 95],
    2: [8, 27],
    3: [12, 18, 20, 28, 44, 45, 50, 52, 63, 68, 75, 76, 92, 98, 99],
    4: [16, 30, 42, 66, 70, 78, 81],
    6: [24, 32, 40, 54, 56, 88],
    8: [36, 72],
    10: [60, 64, 84, 90],
    11: [48, 80],
    18: [96]
}


def is_prime(number): return all([number % i for i in range(2, number)])


PRIMES = [i for i in range(2, 100) if is_prime(i) == True]


def prod_int_part(n):
    assert n <= 100
    a = number_of_products(n)
    b = prime_factorization(n)
    return [a, b]


def number_of_products(n):
    for number in product_numbers:
        if n in product_numbers[number]:
            return number
    return 0


def prime_factorization(number):
    if number in PRIMES:
        return []
    result = []
    prime_factors = [prime for prime in PRIMES if number % prime == 0]
    for factor in prime_factors:
        while number % factor == 0:
            result.append(factor)
            number = number // factor
    return result
