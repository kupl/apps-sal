import random as r
number=r.randint(-12,46)
b=r.randint(-5,6)
c=r.randint(-6,16)
def is_divide_by(number, b, c):
    if number%b == 0 and number%c == 0:
        return True
    else:
        return False 
