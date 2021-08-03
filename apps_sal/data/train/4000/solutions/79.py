from math import factorial


def strong_num(number):
    fact_digits = sum(factorial(int(i)) for i in str(number))
    return "STRONG!!!!" if fact_digits == number else "Not Strong !!"
