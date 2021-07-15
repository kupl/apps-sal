def count_repeats(txt):
    a = 0
    for i in range(0, len(txt) - 1):
        if txt[i] == txt[i + 1]:
            a += 1
    return a
