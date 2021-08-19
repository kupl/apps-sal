def create_anagram(s, t):
    return sum((max(t.count(c) - s.count(c), 0) for c in set(t)))
