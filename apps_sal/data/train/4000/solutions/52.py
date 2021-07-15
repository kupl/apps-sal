def factorial(n):
    ret = 1
    for i in range(1, n + 1):
        ret *= i
    return ret

def strong_num(number):
    if sum([factorial(int(i)) for i in str(number)]) == number:
        return 'STRONG!!!!'
    else:
        return 'Not Strong !!'
