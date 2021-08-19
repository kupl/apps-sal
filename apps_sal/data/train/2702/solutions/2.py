def create_anagram(s, t):
    for c in s:
        t = t.replace(c, '', 1)
    return len(t)
