def spoonerize(words):
    h = [x[0] for x in words.split()]
    t = [y[1:] for y in words.split()]
    return ' '.join(x+y for x,y in zip(h[::-1],t))
