from math import exp, floor
def ex_euler(n):
    y = 1
    x = 0
    T = 1/n
    error = 0
    
    for i in range (n):
        y = y + (2 - exp(-4*x) - 2*y)*T 
        x = x + T
        zk = (1 + 0.5 * exp(-4*x) - 0.5 * exp(-2*x))
        error = error + abs(y - zk)/zk
    return floor(error/(n+1) * 10 ** 6 )/10 ** 6
#float("{:.6f}".format(error/(n+1)))
#round(error/(n+1),6)

