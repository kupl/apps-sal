def isomorph(a, b):
    return len(a) == len(b) and len(set(a)) == len(set(b)) == len(set(zip(a, b)))
