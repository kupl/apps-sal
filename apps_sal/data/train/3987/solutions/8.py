def spin_words(s): return ' '.join([
    len(w) > 4 and w[::-1] or w
    for w in s.split()
])
