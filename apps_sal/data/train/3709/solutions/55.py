from math import *
def simple_multiplication(number) :
    if fmod(int(number), 2) == 0:
        even = True
    else:
        even = False

    if even == True:
        return int(number) * 8
    else:
        return int(number) * 9
