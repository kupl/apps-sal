def scramble(s1, s2):
    c = {item: s1.count(item) for item in set(s1)}
    d = {item: s2.count(item) for item in set(s2)}
    for item in d:
        e = c.get(item) or None
        if not e or e < d.get(item):
            return False
    return True
