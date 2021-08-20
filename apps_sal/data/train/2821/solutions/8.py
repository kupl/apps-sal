H = {'J': '|', '|': '|', '...': '...'}


def trim(b):
    return [[H[h] for h in m] for m in b[:-1]] + [['...'] * len(b[-1])]
