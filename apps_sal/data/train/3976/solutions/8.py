def last(*args):
    last = args[-1]
    try:
        return last[-1]
    except TypeError:
        return last
