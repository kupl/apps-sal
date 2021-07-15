def triple_trouble(one, two, three):
    return ''.join([j for i in zip(*[one, two, three]) for j in i])
