def levenshtein(a,b):
    def recurse(i, j):
        if i >= len(a) or j >= len(b):
            return abs(i - len(a)) + abs(j - len(b))
        if a[i] == b[j]:
            return recurse(i+1, j + 1)
        else:
            return 1 + min(recurse(i + 1, j), recurse(i, j + 1), recurse(i + 1, j + 1))
    return recurse(0,0)
