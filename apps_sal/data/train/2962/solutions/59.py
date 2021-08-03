def divisible_by(numbers, divisor):
    l1 = []
    for i in range(len(numbers)):
        if numbers[i] % divisor == 0:
            l1.append(numbers[i])
    return l1
