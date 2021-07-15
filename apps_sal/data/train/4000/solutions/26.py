from math import factorial

def strong_num(number):
    arr = [int(i) for i in str(number)]
    x = 0 
    for i in arr:
        x += factorial(i)
    if x == number:
        return "STRONG!!!!"
    return "Not Strong !!"
