import string


def compare(s1, s2):

    def numerise(s):
        if not s:
            return 0
        res = 0
        for k in s.upper():
            if k not in string.ascii_letters:
                return 0
            res += ord(k)
        return res
    return numerise(s1) == numerise(s2)
