def triple_trouble(one, two, three):
    zipped = list(zip(one, two, three))
    return ''.join('%s%s%s' % z for z in zipped)
