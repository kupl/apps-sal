from math import sin, pi

def simpson(n, a=0, b=pi):
    f = lambda x: 1.5 * sin(x)**3
    h = (b-a)/n
    return (h/3 * (f(a) + f(b) 
                   + 4 * sum( f(a + (2*i-1) * h) for i in range(1, n//2 +1))
                   + 2 * sum( f(a + 2*i*h) for i in range(1, n//2))))
