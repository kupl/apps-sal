import math
    
def strong_num(number):
    n = str(number)
    return 'STRONG!!!!' if sum(math.factorial(int(a)) for a in n) == number else 'Not Strong !!'
