def reverse_words(text):
    L = []
    a = text.split(" ")
    for i in a:
        i = i[::-1]
        L.append(i)
    x = " ".join(L)
    return x
