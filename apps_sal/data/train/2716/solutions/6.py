CYPHER = tuple(zip('aeiou', '12345'))


def munge(st, mapping):
    return ''.join([mapping.get(c, c) for c in st])


def encode(st):
    return munge(st, {a: b for (a, b) in CYPHER})


def decode(st):
    return munge(st, {b: a for (a, b) in CYPHER})
