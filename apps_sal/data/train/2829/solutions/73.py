def array_madness(a, b):
    a_total = 0
    b_total = 0

    for i in a:
        x = i * i
        a_total += x

    for i in b:
        x = i * i * i
        b_total += x

    return a_total > b_total
