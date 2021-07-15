def word_count(s):
    return sum(1 for w in "".join(c if c.isalpha() else " " for c in s.lower()).split() if w not in ["a", "the", "on", "at", "of", "upon", "in", "as"])
