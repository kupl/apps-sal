def tv_remote(word):
    letters = {c: (x, y)
        for y, row in enumerate((
        "abcde123",
        "fghij456",
        "klmno789",
        "pqrst.@0",
        "uvwxyz_/"))
        for x, c in enumerate(row)}
    return sum(
        abs(letters[c1][0] - letters[c2][0]) +
        abs(letters[c1][1] - letters[c2][1]) + 1
        for c1, c2 in zip("a" + word, word))
