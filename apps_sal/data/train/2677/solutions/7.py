import  re
def tv_remote(words):
    letters = {c: (x, y)
        for y, row in enumerate((
        "abcde123",
        "fghij456",
        "klmno789",
        "pqrst.@0",
        "uvwxyz_/",
        "⇧ "))
        for x, c in enumerate(row)}
    words = re.sub(r'((?:^|[a-z])[^A-Z]*)([A-Z])', r'\1⇧\2', words)
    words = re.sub(r'([A-Z][^a-z]*)([a-z])', r'\1⇧\2', words)
    words = words.lower()
    return sum(
        min(abs(letters[c1][0] - letters[c2][0]),8-abs(letters[c1][0] - letters[c2][0])) +
        min(abs(letters[c1][1] - letters[c2][1]),6-abs(letters[c1][1] - letters[c2][1])) + 1
        for c1, c2 in zip("a" + words, words))
