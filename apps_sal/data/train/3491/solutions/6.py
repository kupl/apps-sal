def substring(s, n=2):
    substr, letters, indexes = '', [''] * n, {'': 0}
    for i, c in enumerate(s, 1):
        if c not in letters:
            letters = letters[1:] + [c]
            indexes[c] = i-1
        if i - indexes[letters[0]] > len(substr):
            substr = s[indexes[letters[0]]: i]
    return substr
