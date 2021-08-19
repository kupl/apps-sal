def array_leaders(numbers):
    return [x for (pos, x) in enumerate(numbers) if x > sum(numbers[pos + 1:])]
