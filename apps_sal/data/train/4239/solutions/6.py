def filter_even_length_words(words):
    arr = []
    for el in words:
        if len(el) % 2 == 0:
            arr.append(el)
    return arr
