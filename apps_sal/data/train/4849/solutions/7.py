from string import whitespace, maketrans


def convert_whitespace(s):
    return s.translate(maketrans(whitespace, ' ' * len(whitespace)))


def my_very_own_split(strng, sep=None):
    (start, fil) = (0, False)
    if sep == '':
        raise ValueError('empty separator')
    if sep is None:
        (sep, fil, strng) = (' ', True, convert_whitespace(strng))
    while start <= len(strng):
        end = strng.find(sep, start)
        if end < 0:
            end = len(strng)
        if not fil or strng[start:end]:
            yield strng[start:end]
        start = end + len(sep)
