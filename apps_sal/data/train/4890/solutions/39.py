def find_difference(a, b):
    a_rez = 1
    b_rez = 1
    for x in a:
        a_rez = a_rez * x
    for y in b:
        b_rez = b_rez * y
    return abs(a_rez - b_rez)
