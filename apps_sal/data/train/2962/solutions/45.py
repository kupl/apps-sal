def divisible_by(numbers, divisor):
    i = 0
    check = []
    while i < len(numbers):
        if numbers[i] % divisor == 0:
            check.append(numbers[i])
        i += 1
    return check
