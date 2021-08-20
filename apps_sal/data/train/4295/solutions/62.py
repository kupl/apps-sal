def balanced_num(number):
    number = [int(n) for n in str(number)]
    sleft = 0
    sright = 0
    while len(number) > 2:
        sleft += number.pop(0)
        sright += number.pop(-1)
    return 'Balanced' if sleft == sright else 'Not Balanced'
