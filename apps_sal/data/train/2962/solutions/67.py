def divisible_by(numbers: list, divisor: int) -> list:
    return [x for x in numbers if x % divisor == 0]
