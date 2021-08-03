def simple_multiplication(number):
    if number % 2 == 0 or number == 0:
        return number * 8
    elif number % 2 != 0 or number == 1:
        return number * 9
