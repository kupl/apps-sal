from math import factorial
def pascal(p):
    return [[int((factorial(p)/(factorial(k)*factorial(p-k)))) for k in range(0,p+1)] for p in range(0,p)]
