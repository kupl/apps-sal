def array_leaders(numbers):
    return [numbers[i] for i in range(len(numbers)) if numbers[i] > sum(numbers[i + 1:])]
