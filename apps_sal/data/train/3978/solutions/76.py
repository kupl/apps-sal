def check_for_factor(base, factor):
    a = base % factor  # your code here
    if a == 0:
        c = True
    else:
        c = False
    return c
