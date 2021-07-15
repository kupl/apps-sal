def divisible_by(numbers, divisor):
    hold = []
    for i in range(len(numbers)):
        if numbers[i] % divisor == 0:
            hold.append(numbers[i])
    return hold
