def triple_trouble(one, two, three):
    return ''.join(''.join(el) for el in zip(one, two, three))
