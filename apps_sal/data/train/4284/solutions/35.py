def array_leaders(numbers):
    return [el for i, el in enumerate(numbers) if el > sum(numbers[i + 1:])]
