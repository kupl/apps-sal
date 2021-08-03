def reverse_words(text):
    new = text.split(' ')
    for elem, text in enumerate(new):
        new[elem] = text[::-1]
    return ' '.join(new)
