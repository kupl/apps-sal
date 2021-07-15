def find_average(args):
    sum = 0
    for i in args:
        sum += args[i - 1]
    return sum / len(args)
