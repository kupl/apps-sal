def triple_trouble(one, two, three):
    return ''.join((''.join(i) for i in zip(one, two, three)))
