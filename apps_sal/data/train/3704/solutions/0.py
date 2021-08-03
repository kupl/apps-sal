from itertools import count


def solve_for_x(equation):
    return next(x for n in count(0) for x in [n, -n] if eval(equation.replace("x", str(x)).replace("=", "==")))
