def scramble(s1, s2):
    it = iter(sorted(s1))
    return all(c in it for c in sorted(s2))
