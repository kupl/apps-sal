def char_concat(word):
    m = (len(word) + 2) // 2
    return ''.join((a + b + str(i) for (i, (a, b)) in enumerate(zip(word[:m], word[-1:-m:-1]), 1)))
