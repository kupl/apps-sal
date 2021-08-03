def compress(sentence):
    ref = []
    for x in sentence.lower().split():
        if x not in ref:
            ref.append(x)
    return ''.join([str(ref.index(n)) for n in sentence.lower().split()])
