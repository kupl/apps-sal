def palindrome_pairs(a):
    return [[i, j] for (i, s) in enumerate(a) for (j, t) in enumerate(a) if i != j and str(s) + str(t) == (str(s) + str(t))[::-1]]
