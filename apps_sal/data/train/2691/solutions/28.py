def solve(s):
    return max(list(map(int, ''.join([c if not c.isalpha() else ' ' for c in s]).split())))

