def compare(s1, s2):

    def cmp(s):
        return sum((ord(a) for a in s.upper())) if s and s.isalpha() else 0
    return cmp(s1) == cmp(s2)
