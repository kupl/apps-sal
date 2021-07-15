def array_leaders(numbers):
    return [x for i, x in enumerate(numbers) if x > sum(numbers[i+ 1:])]

