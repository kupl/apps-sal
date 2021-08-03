def divisible_by(numbers, divisor):
    factors = []
    for n in numbers:
        if n % divisor == 0:
            factors.append(n)
    return factors
