import math
from fractions import Fraction 

def expand(x, digit):   
    answer = Fraction(1, 1)
    n = 1
    
    while len(str(answer.numerator)) < digit:
        answer += Fraction(Fraction(str(x))**n, math.factorial(n))
        n += 1
        
    f_answer = [answer.numerator, answer.denominator]
    return f_answer
