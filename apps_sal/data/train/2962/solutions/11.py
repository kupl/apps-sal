def divisible_by(numbers, divisor):
    result = []
    for num in numbers:
        if num % divisor == 0:
            result.append(num)
    return result
