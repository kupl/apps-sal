def triple_trouble(one, two, three):
    from functools import reduce
    return ''.join(reduce(lambda x, y: x + y, zip(one, two, three)))
