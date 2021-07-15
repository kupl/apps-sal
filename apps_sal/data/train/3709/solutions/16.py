def simple_multiplication(number) :
    return number*(9 if number % 2 else 8)

def simple_multiplication(number) :
    return number*(9 if number & 1 else 8)

def simple_multiplication(number) :
    return number*(8 + (number & 1))

