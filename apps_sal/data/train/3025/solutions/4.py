def locate(seq, value):
    if isinstance(seq, (tuple, list)):
        return any((locate(x, value) for x in seq))
    return seq == value
