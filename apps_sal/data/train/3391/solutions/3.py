def flatten(*args):
    result = []
    for arg in args:
        if type(arg) is list:
            result.extend(flatten(*arg))
        else:
            result.append(arg)
    return result
