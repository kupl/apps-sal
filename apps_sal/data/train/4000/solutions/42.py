import math
def strong_num(x):
    return 'STRONG!!!!' if [sum((math.factorial(int(i)))for i in str(x))]==[x] else 'Not Strong !!'
