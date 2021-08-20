def remove_duplicate_words(s):
    res = []
    s = s.split()
    visited = set()
    for w in s:
        if w not in visited:
            res.append(w)
            visited.add(w)
    return ' '.join(res)
