def divisible_by(numbers, divisor):
    return list(map(int, filter(lambda number: number % divisor == 0, numbers)))
