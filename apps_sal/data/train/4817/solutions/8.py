def spread(func, *args):
    x, y, z = 0, 0, 0
    # based on the number of arguments unpack the tuple 'args'
    if len(args[0]) == 2:
        x, y = args[0][0], args[0][1]
        return func(x, y)
    elif len(args[0]) == 3:
        x, y, z = args[0][0], args[0][1], args[0][2]
        return func(x, y, z)
