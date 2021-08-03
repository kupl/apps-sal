def divisible_by(numbers, divisor):
    divNums = []
    for i in numbers:
        if i % divisor == 0:
            divNums.append(i)
    return divNums
