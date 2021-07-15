def triple_trouble(one, two, three):
    return ''.join(''.join(v) for v in zip(one,two,three))
