def sum_of_minimums(numbers):
    som = 0
    for element in numbers:
        som += min(element)
    return som
