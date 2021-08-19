def compress(sentence):
    s = sentence.lower().split()
    sl = []
    for x in s:
        if x not in sl:
            sl.append(x)
    return ''.join((str(sl.index(x)) for x in s))
