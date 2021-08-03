def sort_it(words, i):
    return ", ".join(sorted(words.split(", "), key=lambda w: w[i - 1]))
