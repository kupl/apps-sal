from functools import reduce
def remove_duplicate_words(s):
    return ' '.join(reduce(lambda l, x: l+[x] if x not in l else l, s.split(' '), []))
