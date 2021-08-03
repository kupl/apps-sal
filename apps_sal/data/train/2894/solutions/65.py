def triple_trouble(one, two, three):
    return ''.join(''.join(tuple) for tuple in list(zip(one, two, three)))
