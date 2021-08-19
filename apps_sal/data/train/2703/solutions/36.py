from functools import reduce


def square_sum(numbers):
    if len(numbers) == 0:
        return 0
    else:
        squared = [n ** 2 for n in numbers]
        return reduce(lambda x, y: x + y, squared)
