def simple_multiplication(number):
    total = number * 9
    if number % 2 == 0:
        total = total - number
    return total
