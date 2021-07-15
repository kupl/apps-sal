def array_leaders(numbers):
    return [numbers[x] for x in range(len(numbers)) if sum(numbers[x + 1:]) < numbers[x]]

