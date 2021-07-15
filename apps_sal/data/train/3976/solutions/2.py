def last(*x):
    try:
        return x[-1][-1]
    except TypeError:
        return x[-1]
