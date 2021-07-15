from math import exp
def ex_euler(n):
    f = lambda x, y: 2 - exp(-4*x) - 2*y
    exact = lambda x: 1 + 0.5*exp(-4*x) - 0.5*exp(-2*x)
    x, y, T = 0, 1, 1
    h = T/n
    mx = [0]
    for _ in range(n):    
        y += h*f(x, y)
        x += h
        z = exact(x)
        mx.append(abs(y-z)/z)
    return float(str(sum(mx)/(n+1))[:8])
