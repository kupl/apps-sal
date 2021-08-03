def strong_num(number):
    import math
    sum = 0
    for i in str(number):
        sum = sum + math.factorial(int(i))
    if sum == int(number):
        return "STRONG!!!!"
    else:
        return "Not Strong !!"
