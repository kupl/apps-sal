from itertools import permutations


def get_words(hash):
    chars = ''
    for (k, v) in list(hash.items()):
        chars += ''.join(v) * k
    return sorted(set((''.join(p) for p in permutations(chars))))
