def palindrome_pairs(words):
    w = list(map(str, words))
    return [[i, j] for (i, a) in enumerate(w) for (j, b) in enumerate(w) if i != j and a + b == (a + b)[::-1]]
