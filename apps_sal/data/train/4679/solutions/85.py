def to_freud(x):
    s = x.split()
    d = ['sex ' * len(s)]
    return x if x == '' else ' '.join(d)[:-1]
