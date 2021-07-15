import math as m
def true_binary(n):
    c = 1
    c = m.ceil(m.log(n,2))
    if c == 0:
        c = 1
    n = (n+(2**c-1))//2

    return [(char == '1')*2-1 for char in bin(n)[2:]]
