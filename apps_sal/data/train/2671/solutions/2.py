from re import sub


def cat_mouse(s, j):
    if set(s) < set('mCD.'):
        return 'boring without all three'

    between = sub('.*[Cm](.*?)[Cm].*', r'\1', s)

    if len(between) > j:
        return 'Escaped!'

    if 'D' in between:
        return 'Protected!'

    return 'Caught!'
