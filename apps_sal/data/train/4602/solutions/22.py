def is_anagram(a, b, s=sorted): return s(a.lower()) == s(b.lower())
