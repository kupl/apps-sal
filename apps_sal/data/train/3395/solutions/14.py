def remove_duplicate_words(s):
    l = s.split()
    words = []
    for elt in l:
        if elt not in words:
            words.append(elt)
    return " ".join(words)
