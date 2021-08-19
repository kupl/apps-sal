def levenshtein(a, b):
    if len(a) == 0:
        return len(b)
    if len(b) == 0:
        return len(a)
    if a[0] == b[0]:
        dist = 0
    else:
        dist = 1
    return min(levenshtein(a[1:], b) + 1, levenshtein(a, b[1:]) + 1, levenshtein(a[1:], b[1:]) + dist)
