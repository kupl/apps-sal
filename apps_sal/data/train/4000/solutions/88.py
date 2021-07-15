from math import factorial

def strong_num(number):
    return ["Not Strong !!", "STRONG!!!!"][sum(map(lambda x: factorial(int(x)), str(number))) == number]
