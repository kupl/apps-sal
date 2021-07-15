def game(n):
    numerator = n ** 2
    denominator = 2
    if numerator % denominator == 1:
        return [numerator, denominator]
    return [numerator // denominator]
