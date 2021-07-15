from collections import Counter

def group(a):
    return sorted([[k]*v for k, v in Counter(a).items()], key=lambda k: a.index(k[0]))
