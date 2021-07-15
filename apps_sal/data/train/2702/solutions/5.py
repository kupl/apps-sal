def create_anagram(s, t):
    return sum(abs(s.count(c)-t.count(c))for c in set(s+t))/2
