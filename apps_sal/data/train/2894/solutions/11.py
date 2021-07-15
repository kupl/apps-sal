def triple_trouble(one, two, three):
    return ''.join(''.join(s) for s in zip(one, two, three))
