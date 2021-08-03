def word_pattern(pattern, string):
    x = list(pattern)
    y = string.split(" ")
    return (len(x) == len(y) and
            len(set(x)) == len(set(y)) == len(set(zip(x, y)))
            )
