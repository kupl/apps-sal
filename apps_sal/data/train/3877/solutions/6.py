layout = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
letters = {c: str(n) for n, cs in enumerate(layout) for c in cs}

def T9(words, seq):
    return ([word for word in words if ''.join(letters[c] for c in word.lower()) == seq]
            or [''.join(layout[i][0] for i in map(int, seq))])
