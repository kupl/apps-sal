def compress(sentence):
    ref = []
    for i in sentence.lower().split():
        if i not in ref:
            ref.append(i)
    return ''.join([str(ref.index(n)) for n in sentence.lower().split()])
