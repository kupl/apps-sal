from math import isclose


def you_are_a_cube(cube):
    return isclose(cube**(1.00 / 3.00) % 1, 1, rel_tol=0.0001) or isclose(cube**(1.00 / 3.00) % 1, 0, rel_tol=0.0001)
