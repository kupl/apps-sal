def sort_word(w, l):
    return (lambda a: ''.join((next(a) if c.isalpha() else c for c in w)))(iter(l[:len(l) > 1] + sorted(l[1:-1]) + l[-1:]))


def scramble_words(s):
    return ' '.join((sort_word(w, list(filter(str.isalpha, w))) for w in s.split()))
