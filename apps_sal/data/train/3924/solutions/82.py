def reverse_words(text):
    a = text.split(' ')
    b = []
    for word in a:
        b.append(word[::-1])
    c = ' '.join(b)
    return c
