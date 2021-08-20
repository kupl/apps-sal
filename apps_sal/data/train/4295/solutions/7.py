def balanced_num(n):
    return 'Balanced' if sum([int(x) for x in str(n)[:int(len(str(n)) / 2 - 0.5)]]) == sum([int(x) for x in str(n)[int(len(str(n)) / 2 + 1):]]) else 'Not Balanced'
