def divisible_by(numbers, divisor):
    factors = []
    for divisible in numbers:
        if divisible % divisor == 0:
            factors.append(divisible)
    return factors
