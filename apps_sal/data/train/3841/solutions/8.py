from itertools import permutations
def get_words(h):
    return [''.join(p) for p in sorted(set(permutations(''.join([letter * key for key in h for letter in h[key]]))))]
