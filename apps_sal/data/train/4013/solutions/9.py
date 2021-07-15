def spoonerize(words):
    l, r = words.split()
    return r[0] + l[1:] + ' ' + l[0] + r[1:]
