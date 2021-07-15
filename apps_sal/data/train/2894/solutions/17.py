def triple_trouble(*l):
    return ''.join([''.join(s) for s in zip(*l)])
