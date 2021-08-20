import collections


def duplicate_encode(word):
    new_string = ''
    word = word.lower()
    d = collections.defaultdict(int)
    for c in word:
        d[c] += 1
    for c in word:
        new_string = new_string + ('(' if d[c] == 1 else ')')
    return new_string
