def isomorph(a, b):
    return len(a) == len(b) and a.translate(str.maketrans(a, b)) == b and (b.translate(str.maketrans(b, a)) == a)
