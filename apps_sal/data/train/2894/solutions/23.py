from itertools import chain
def triple_trouble(one, two, three):
    return ''.join(c for c in chain.from_iterable(zip(one,two,three)))
