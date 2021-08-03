def remove_duplicate_words(s):
    t = set()
    s = s.split()
    r = []
    for w in s:
        if w not in t:
            t.add(w)
            r.append(w)
    return ' '.join(r)
