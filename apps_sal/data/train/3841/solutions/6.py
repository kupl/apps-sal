def get_words(d):
    from itertools import permutations
    s = ''
    for key in d:
        for char in d[key]:
            s += char * key
    p = permutations(s, len(s))
    return sorted(list(set([''.join(word) for word in p])))
