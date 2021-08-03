def not_so_random(b, w):
    if b % 2 == 0 and w % 2 == 0:
        return "White"
    elif b % 2 == 1 and w % 2 == 0:
        return "Black"
    elif b % 2 == 1 and w % 2 == 1:
        return "Black"
    elif b % 2 == 0 and w % 2 == 1:
        return "White"
