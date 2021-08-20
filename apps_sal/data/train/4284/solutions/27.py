def array_leaders(numbers):
    p = [j for (i, j) in enumerate(numbers) if j > sum(numbers[i + 1:])]
    return p
