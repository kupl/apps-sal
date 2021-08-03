from itertools import chain


def capitals_first(text):
    cap, low = [], []
    for w in text.split():
        if w[0].isalpha():
            (cap, low)[w[0].islower()].append(w)
    return ' '.join(chain(cap, low))
