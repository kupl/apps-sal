def unpack(l):
    """Unpack a list of elements that contains unpackable objects.

    >>> unpack([None, [1, ({2, 3}, {'foo': 'bar'})]])
    [None, 1, 2, 3, 'foo', 'bar']

    """
    res = []
    for i in l:
        if type(i) is list:
            res += unpack(i)
        elif type(i) is tuple:
            res += unpack(list(i))
        elif type(i) is dict:
            res += unpack(list(i.keys()))
            res += unpack(list(i.values()))
        elif type(i) is set:
            res += unpack(list(i))
        else:
            res += [i]
    return res

