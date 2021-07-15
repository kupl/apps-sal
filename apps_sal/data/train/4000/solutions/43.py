import math

def strong_num(number):
    return "STRONG!!!!" if number == sum(math.factorial(int(c)) for c in str(number)) else "Not Strong !!"

