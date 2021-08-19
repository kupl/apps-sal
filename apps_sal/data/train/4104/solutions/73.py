def max_tri_sum(numbers):
    numbers = set(numbers)
    numbers = list(numbers)
    n1 = numbers.pop(numbers.index(max(numbers)))
    n2 = numbers.pop(numbers.index(max(numbers)))
    n3 = numbers.pop(numbers.index(max(numbers)))
    return sum((n1, n2, n3))
