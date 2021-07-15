import math
def strong_num(number):
    if number == sum([math.factorial(int(d)) for d in str(number)]):
        return "STRONG!!!!"
    else:
        return "Not Strong !!"
