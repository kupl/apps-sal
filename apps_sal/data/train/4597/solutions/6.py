def combine(*args):
    result = []
    l = len(max(args, key=len))
    for loop in range(l):
        result.extend((array[loop] for array in args if len(array) > loop))
    return result
