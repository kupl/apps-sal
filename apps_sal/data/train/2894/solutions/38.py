def triple_trouble(one, two, three):
    return ''.join(''.join(set) for set in list(zip(one, two, three)))
