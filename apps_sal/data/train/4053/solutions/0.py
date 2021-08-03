def reverse_factorial(num):
    c = f = 1
    while f < num:
        c += 1
        f *= c
    return 'None' if f > num else "%d!" % c
