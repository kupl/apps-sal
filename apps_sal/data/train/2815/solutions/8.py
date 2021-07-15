def compress(sentence):
    l = sentence.lower().split()
    u = [s for i,s in enumerate(l) if l.index(s)==i]
    return ''.join(str(u.index(s)) for s in l)
