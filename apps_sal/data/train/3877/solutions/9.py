mapping = {'2': "abc",
           '3': "def",
           '4': "ghi",
           '5': "jkl",
           '6': "mno",
           '7': "pqrs",
           '8': "tuv",
           '9': "wxyz"}


def T9(words, seq):
    return [word for word in words if len(word) >= len(seq) and all(word[i].lower() in mapping[n] for i, n in enumerate(seq))] or ["".join(mapping[i][0] for i in seq)]
