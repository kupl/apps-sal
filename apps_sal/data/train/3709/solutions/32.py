def simple_multiplication(number):
    #     return number * 8 if number%2 == 0 else number * 9
    return number * (9, 8)[number % 2 == 0]
