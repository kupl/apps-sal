def make_sentences(parts):
    n = ''
    parts = [i for i in parts if i != '.']
    for i in parts:
        if i == ',':
            n = n[:-1] + ', '
        else:
            n += i + ' '
    return n[:-1]+'.'
