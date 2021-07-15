def balanced_num(number):
    number = str(number)
    if len(number) >= 3:
        return 'Balanced' if sum([int(x) for x in number[0:round(len(number) / 2 + .49) - 1]]) == sum([int(x) for x in number[-round(len(number) / 2 + .49) + 1:]]) else 'Not Balanced'
    else:
        return 'Balanced'
