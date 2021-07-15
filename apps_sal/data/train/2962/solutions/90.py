def divisible_by(numbers, divisor):
    lst = []
    for i in numbers:
        if i % divisor == False:
            lst.append(i)
    return lst
