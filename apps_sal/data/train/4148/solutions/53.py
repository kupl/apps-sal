def sum_digits(number):
    sum_digits = 0
    number2 = abs(number)
    for i in str(number2):
        sum_digits += int(i)
    return sum_digits
