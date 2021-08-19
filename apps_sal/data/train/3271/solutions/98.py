def arr(*args):
    array = []
    if args:
        for i in range(args[0]):
            array.append(i)
    return array
