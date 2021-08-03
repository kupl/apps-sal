def combine(*args):
    rez = {}

    for i in args:
        for k, v in i.items():
            rez[k] = rez.get(k, 0) + v

    return rez
