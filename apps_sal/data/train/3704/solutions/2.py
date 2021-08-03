def solve_for_x(equation):
    left_side = equation.split('=')[0]
    right_side = equation.split('=')[1]

    for x in range(-1000, 1000):
        if eval(left_side) == eval(right_side):
            return x
