def riemann_trapezoidal(f, n, a, b):
    delta_x = (b - a) / float(n)
    def middle_height(i): return (f(a + i * delta_x) + f(a + (1 + i) * delta_x)) / 2
    arr = map(middle_height, xrange(n))
    return round(sum(arr) * delta_x, 2)
