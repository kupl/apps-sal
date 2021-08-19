def T9(words, seq):
    (X, res) = (['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz'], '')
    for (i, c) in enumerate(map(int, seq)):
        words = [w for w in words if w[i].lower() in X[c]]
        res += X[c][0]
    return words or [res]
