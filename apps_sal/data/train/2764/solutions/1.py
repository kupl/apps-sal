from math import sqrt


def nb_sol_cube_is_sumsq(c):
    count = 0
    c3 = c ** 3
    modc3 = c3 % 4
    if modc3 == 3 or modc3 == 2:
        return 0
    for a in range(1, int(sqrt(c ** 3)) + 1):
        b = sqrt(c3 - a ** 2)
        if int(b) == b and 0 < b <= a:
            count += 1
    return count


def nb_abc_sol(c_max):
    (res, c) = ([], 1)
    while c <= c_max:
        res.append(nb_sol_cube_is_sumsq(c))
        c += 1
    return res


sol = nb_abc_sol(1001)


def find_abc_sumsqcube(c_max, num_sol):
    return [i + 1 for (i, count) in enumerate(sol[:c_max]) if count == num_sol]
