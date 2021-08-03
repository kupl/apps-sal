def strong_num(number):
    import math
    lst = []
    for i in str(number):
        lst.append(math.factorial(int(i)))
    return 'STRONG!!!!' if sum(lst) == number else 'Not Strong !!'
