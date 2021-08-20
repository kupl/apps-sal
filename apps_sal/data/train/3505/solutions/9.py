from itertools import chain, islice, cycle


def padding(fill, size):
    return islice(cycle(fill), size)


def super_pad(string, width, fill=' '):
    if not width:
        return ''
    if not fill:
        return string[:width]
    size = width - len(string)
    if size <= 0:
        return string[:width] if fill[0] in '>^' else string[-width:]
    if fill[0] == '>':
        return string + ''.join(padding(fill[1:], size))
    if fill[0] == '^':
        return ''.join(padding(fill[1:], size + 1 >> 1)) + string + ''.join(padding(fill[1:], size >> 1))
    if fill[0] == '<':
        fill = fill[1:]
    return ''.join(padding(fill, size)) + string
