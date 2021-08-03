def solve_for_x(equation):
    p = equation.split()
    for i in range(0, len(p)):
        if p[i] == '=':
            p[i] = '=='
    t = p.index('x')
    for x in range(-100, 1000):
        p[t] = str(x)
        if eval(''.join(p)):
            return x
