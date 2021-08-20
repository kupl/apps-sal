def isomorph(a, b):

    def normalize(s):
        return [s.index(c) for c in s]
    return normalize(a) == normalize(b)
