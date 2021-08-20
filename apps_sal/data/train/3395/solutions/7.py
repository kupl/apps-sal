d = {}


def remove_duplicate_words(s):
    return ' '.join((d.setdefault(w, w) for w in s.split() if w not in d))
