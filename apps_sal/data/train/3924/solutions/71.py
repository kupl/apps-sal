def reverse_words(text):
    medzera = ' '
    x = text.split(medzera)
    for i in range(len(x)):
        x[i] = x[i][::-1]
    y = medzera.join(x)
    return y
