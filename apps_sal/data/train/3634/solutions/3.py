def reverse_it(data):
    t = type(data)
    if t not in (str, float, int):
        return data
    return t(str(data)[::-1])
