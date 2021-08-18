def solve_for_x(equation):
    for x in range(-100, 1001):
        if eval(equation.replace('=', '==')):
            return x
