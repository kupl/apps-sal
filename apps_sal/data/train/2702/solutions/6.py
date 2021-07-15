def create_anagram(s, t):
    for a in s:
        t = t.replace(a, '', 1)
    return len(t)
