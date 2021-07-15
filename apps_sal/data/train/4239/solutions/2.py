def filter_even_length_words(words):
    ret = []
    for w in words:
        if len(w) % 2 == 0:
            ret.append(w)
    return ret
