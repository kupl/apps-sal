upper = __import__("string").ascii_uppercase.__getitem__


def get_column_title(num=None):
    if not isinstance(num, int):
        raise TypeError()
    if num < 1:
        raise IndexError()
    res = []
    while num:
        num, r = divmod(num - 1, 26)
        res.append(r)
    return ''.join(map(upper, reversed(res)))
