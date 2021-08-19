def sum_digits(number):
    sum = 0
    for e in str(abs(number)):
        sum += int(e)
    return sum
