def sum_digits(number):
    sum = 0
    while abs(number) // 10 != 0:
        sum += abs(number) % 10
        number = abs(number) // 10
    sum += abs(number) % 10
    return sum
