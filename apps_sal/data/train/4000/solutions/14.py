from math import factorial


def strong_num(number):
    strong = number == sum((factorial(int(digit)) for digit in str(number)))
    return 'STRONG!!!!' if strong else 'Not Strong !!'
