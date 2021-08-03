def compare(s1, s2):
    def calc(s):
        if not s or not all(map(lambda c: c.isalpha(), s)):
            return 0
        return sum(ord(c) for c in s.upper())
    return calc(s1) == calc(s2)
