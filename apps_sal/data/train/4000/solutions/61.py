from math import factorial
def strong_num(number):
    a=0
    for i in str(number):
       a+=factorial(int(i))
    if a==number:
       return 'STRONG!!!!'
    return 'Not Strong !!'
