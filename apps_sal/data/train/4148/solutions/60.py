def sum_digits(number):
    sum = 0
    for i in list(str(abs(number))):
        sum = sum + int(i)

    return sum
