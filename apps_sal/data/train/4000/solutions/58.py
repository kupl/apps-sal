from math import factorial as fact

def strong_num(number):
    return "STRONG!!!!" if sum(fact(int(digit)) for digit in str(number)) == number else "Not Strong !!"
