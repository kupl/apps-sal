def sum_digits(number):
    sum = 0
    for num in str(abs(number)):
        sum += int(num)
    return sum

