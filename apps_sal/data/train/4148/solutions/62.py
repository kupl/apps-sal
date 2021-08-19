def sum_digits(number):
    if number < 0:
        number *= -1
    if number < 10:
        return number
    else:
        last_digit = number % 10
        return sum_digits(number // 10) + last_digit
