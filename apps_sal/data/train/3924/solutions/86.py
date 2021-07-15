def reverse_words(text):
    r = []
    for w in text.split(' '):
        r.append(w[int(len(w))::-1])
    s = ' '
    return s.join(r)

