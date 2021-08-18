from itertools import count


def solve_for_x(equation):
    equation = equation.replace('=', '==')
    for x in count():
        if eval(equation):
            return x
        x = -x
        if eval(equation):
            return x
