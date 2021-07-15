def divisible_by(numbers, divisor):
    x = []
    for i in range(len(numbers)):
        if numbers[i] % divisor == 0:
            x.append(numbers[i])
        else:
            x = x
    return x
