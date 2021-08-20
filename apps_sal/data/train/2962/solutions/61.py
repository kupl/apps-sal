def divisible_by(numbers, divisor):
    result = []
    for el in numbers:
        if not el % divisor:
            result.append(el)
    return result
