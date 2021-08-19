def contamination(s, c):
    return ''.join([x.replace(x, c) for x in s if s != ''])
