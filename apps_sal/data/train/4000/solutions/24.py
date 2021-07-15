import math
def strong_num(number):
    x= [math.factorial(int(x)) for x in str(number) ]
    if number==sum(x):
        return 'STRONG!!!!'
    return 'Not Strong !!'
