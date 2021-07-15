from math import factorial
def am_i_wilson(n):
#    print(n)
    if n<=2: return False
    if n>999: return False
    bob =  (factorial(n-1) +1)
    if  bob//(n*n)*(n*n) == bob: return True
    return False

