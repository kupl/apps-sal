from string import punctuation as p


def camelize(s):
    return ''.join([x.capitalize() for x in reduce(lambda a, kv: a.replace(*kv), [(x, ' ') for x in p], s).split(' ')])
