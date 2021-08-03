def solve_for_x(equation):
    left, right = equation.split('=')
    for x in range(-1000, 1000):
        if eval(left) == eval(right):
            return x
