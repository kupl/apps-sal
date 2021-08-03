def compare(s1, s2):
    def val(s):
        return 0 if s is None or not s.isalpha() else sum(ord(c) for c in s.upper())
    return val(s1) == val(s2)
