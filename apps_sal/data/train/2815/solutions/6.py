def compress(sentence):
    s = []
    for i in sentence.split():
        if i.lower() not in s:
            s.append(i.lower())
    return ''.join([str(s.index(x.lower())) for x in sentence.split()])
