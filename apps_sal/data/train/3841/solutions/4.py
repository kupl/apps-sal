from itertools import permutations


def get_words(dct):
    s = ''.join(c * n for n, lst in dct.items() for c in lst)
    return sorted(set(map(''.join, permutations(s, len(s)))))
