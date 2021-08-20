def product(numbers):
    if not numbers:
        return None
    prod = 1
    for i in numbers:
        prod *= i
    return prod
