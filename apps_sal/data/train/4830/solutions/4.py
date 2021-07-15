def riemann_trapezoidal(f, n, a, b):
    area = 0
    dt = (b-a)/n
    x1 = a
    for i in range(n):
        A1 = f(x1)*dt
        x1 = x1+dt
        A2 = f(x1)*dt
        area += (A1+A2)/2
    return round(area+0.001, 2)
