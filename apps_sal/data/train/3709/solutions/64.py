def simple_multiplication(number):
    return int(''.join(str(number * 8) if number % 2 == 0 else str(number * 9)))
