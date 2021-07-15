def sum_digits(num):
    sum = 0
    for x in str(abs(num)):
        sum += int(x)
    return sum

