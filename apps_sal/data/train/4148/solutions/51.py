def sum_digits(number):
    if number < 0:
        number = number * -1
    total = 0
    while number > 0:
        dig = number % 10
        total += dig
        number = number // 10
    return total
