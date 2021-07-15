def sum_digits(number):
    my_sum = 0
    number = abs(number)
    while number >= 10:
        my_sum = my_sum + (number % 10)
        number = int(number / 10)
    my_sum = my_sum + number
    return my_sum
