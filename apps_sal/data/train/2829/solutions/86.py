def array_madness(a, b):
    a_total = 0
    b_total = 0
    for num in a:
        squares = num ** 2
        a_total = a_total + squares
    for num in b:
        cubes = num ** 3
        b_total = b_total + cubes
    return a_total > b_total
