from math import factorial


def strong_num(N):
    sum = 0
    P = N
    for i in range(len(str(N))):
        sum += factorial(N // 10**(len(str(N)) - 1))
        N = N % (10**(len(str(N)) - 1))
    return "STRONG!!!!" if P == sum else "Not Strong !!"
