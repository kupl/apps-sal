def get_real_floor(n):
    floors = n - 1
    top = n - 2
    basement = n
    if n >= 1 and n < 13:
        return floors
    elif n <= 0:
        return basement
    else:
        return top
