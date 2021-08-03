def evaporator(a, b, c):
    b /= 100
    a_origin = a
    rem = a_origin
    day = 0
    trsh = c / 100
    while rem >= trsh:
        day += 1
        pr = a * b
        a -= pr
        rem = a / a_origin
    return day
