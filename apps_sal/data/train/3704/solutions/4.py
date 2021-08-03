from itertools import count

# Brute force: the solution to all your problems


def solve_for_x(equation):
    equation = equation.replace('=', '==')
    for x in count():
        if eval(equation):
            return x
        x = -x
        if eval(equation):
            return x
