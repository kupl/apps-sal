def correct(string):
    d = dict(zip('015', 'OIS'))
    return ''.join((d.get(c, c) for c in string))
