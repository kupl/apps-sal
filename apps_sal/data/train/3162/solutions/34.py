def compare(s1, s2):
    (v1, v2) = (sum((ord(c) for c in s.upper())) if s and s.isalpha() else 0 for s in (s1, s2))
    return v1 == v2
