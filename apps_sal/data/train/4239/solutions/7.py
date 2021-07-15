def filter_even_length_words(words):
    s = []
    for el in words:
        if len(el) % 2 == 0:
            s.append(el)
    return s
