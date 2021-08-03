def intersperse(delim, s):
    it = iter(s)
    yield next(it)
    for t in it:
        yield delim
        yield t


def two_sort(array):
    return ''.join(intersperse('***', sorted(array)[0]))
