def create_anagram(s, t):
    return sum((max(0, s.count(c) - t.count(c)) for c in set(s)))
