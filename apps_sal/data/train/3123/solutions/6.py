def count_repeats(txt):
    return sum((a == b for (a, b) in zip(txt, txt[1:])))
