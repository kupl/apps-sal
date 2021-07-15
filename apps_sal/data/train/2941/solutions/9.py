def add(*args):
    return round(sum(args[i]/(i+1) for i in range(len(args))))
