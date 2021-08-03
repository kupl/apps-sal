def compare(s1, s2):
    def get_val(s):
        if not s:
            return 0
        v = 0
        for c in s.upper():
            if c.isalpha():
                v += ord(c)
            else:
                return 0
        return v
    return get_val(s1) == get_val(s2)
