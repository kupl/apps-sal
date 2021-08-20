def interweave(s1, s2):
    return ''.join((y for x in zip(s1, s2 + '0') for y in x if not y.isdigit()))
