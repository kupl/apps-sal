def sum_digits(number):
    sum = 0
    if number < 0:
        number = number * -1
    while len(str(number)) != 1:
        sum += number % 10
        number = number // 10
    sum += number
    return sum
