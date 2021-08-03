def divisible_by(numbers, divisor):
    lst = list()
    for number in numbers:
        if number % divisor == 0:
            lst.append(number)
    return lst
