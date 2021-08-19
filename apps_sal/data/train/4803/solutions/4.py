def two_sum(numbers, target):
    for (i, val1) in enumerate(numbers[:-1]):
        for (j, val2) in enumerate(numbers[i + 1:]):
            if val1 + val2 == target:
                return (i, j + i + 1)
