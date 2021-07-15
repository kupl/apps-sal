def flatten(*args):
    return flat([], *args)


def flat(res, *args):
    for arg in args:
        if isinstance(arg, list):
            flat(res, *arg)
        else:
            res.append(arg)
    return res
