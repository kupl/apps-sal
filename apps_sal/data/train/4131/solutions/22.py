def how_much_water(*args):
    if args[2] > args[1] * 2:
        return 'Too much clothes'
    elif args[2] < args[1]:
        return 'Not enough clothes'
    else:
        return round(args[0] * 1.1**(args[2] - args[1]), 2)
