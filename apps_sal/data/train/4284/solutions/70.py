def array_leaders(numbers):
    return [x for (index, x) in enumerate(numbers) if x > sum(numbers[index + 1:])]
