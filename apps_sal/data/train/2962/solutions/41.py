def divisible_by(numbers, divisor):
    result = []
    for digit in numbers:
        if digit % divisor == 0:
            result.append(digit)
    return result
