def reverse_words(text):
    n = len(text)
    liste = text.split(' ')
    liste = [reverse(mot) for mot in liste]
    return ' '.join(liste)


def reverse(text):
    n = len(text)
    reponse = ''
    for i in range(n):
        reponse += text[n - (i + 1)]
    return reponse
