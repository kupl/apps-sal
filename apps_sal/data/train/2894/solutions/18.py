def triple_trouble(*args):
    return ''.join(''.join(tupl) for tupl in zip(*args))
