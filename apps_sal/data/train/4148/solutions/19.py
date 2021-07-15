def sum_digits(number):
    number = str(number)
    numT = 0
    for i in number:
        if i != "-":
            numT += int(i)
    return numT
