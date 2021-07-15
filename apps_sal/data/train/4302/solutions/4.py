def better_than_average(*args):
    return args[1] > sum(*args) / (len(args[0]) + 1.0)
