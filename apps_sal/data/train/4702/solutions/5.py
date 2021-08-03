def prime_factors(num):
    factors = []
    while num % 2 == 0:
        factors.append(2)
        num //= 2

    i = 3
    max_factor = num**0.5
    while i <= max_factor:
        while num % i == 0:
            factors.append(i)
            num //= i
            max_factor = num**0.5
        i += 2

    if num > 1:
        factors.append(num)
    return factors


def digits_product(product):
    if product == 0:
        return 10
    elif product == 1:
        return 11

    factors = prime_factors(product)
    if not set(factors) <= {2, 3, 5, 7}:
        return -1
    if len(factors) == 1:
        return 10 + factors[0]

    factors = "".join(str(f) for f in factors)
    factors = "".join(sorted(factors.replace("33", "9")))
    factors = factors.replace("222", "8")
    factors = factors.replace("23", "6")
    factors = factors.replace("22", "4")
    if len(factors) == 1:
        factors += "1"
    return int("".join(sorted(factors)))
