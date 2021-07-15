def is_triangle(a, b, c):
    tab_coter = [a, b, c]
    tab_coter.sort()
    calc_long_coter = tab_coter[0] + tab_coter[1]
    if (tab_coter[2] < calc_long_coter):
        return True
    return False

