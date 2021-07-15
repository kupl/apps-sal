from math import factorial
def strong_num(n):
    return 'STRONG!!!!' if sum([factorial(int(x)) for x in str(n)])==n else 'Not Strong !!'
