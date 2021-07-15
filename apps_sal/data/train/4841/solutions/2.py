from math import sin, pi

def simpson(n):
    f = lambda x : 1.5*sin(x)**3
    h = pi / float(n)
    s1 = 0
    for i in range(1, int(n / 2) + 1):
        s1 += f((2 * i - 1) * h)
    s2 = 0
    for i in range(1, int(n / 2)):
        s2 += f(2 * i * h)
    res = pi / (3 * n) * (f(0) + f(pi) + 4 * s1 + 2 * s2) 
    return res
