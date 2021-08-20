def sum_digits(number):
    number = abs(number)
    result = 0
    while number > 0:
        result += number % 10
        number //= 10
    return result
