def create_anagram(s, t):
    return sum([s.count(x) - t.count(x) if s.count(x) > t.count(x) else 0 for x in set(s)])
