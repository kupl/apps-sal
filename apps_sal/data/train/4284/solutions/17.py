def array_leaders(numbers):
    return [i for index, i in enumerate(numbers, 1) if sum(numbers[index:]) < i]

