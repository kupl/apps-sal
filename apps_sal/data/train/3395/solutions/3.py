def remove_duplicate_words(s):
    a = []
    [a.append(v) for v in s.split(" ") if v not in a]
    return str(" ").join(a)
