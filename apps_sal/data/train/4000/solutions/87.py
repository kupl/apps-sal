from math import factorial

facs = {str(n):factorial(n) for n in range(10)}

def strong_num(number):
    return 'STRONG!!!!' if number == sum(facs[d] for d in str(number)) else 'Not Strong !!'
