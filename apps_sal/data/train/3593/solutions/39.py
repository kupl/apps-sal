def capitalize(s, ind):
    liste = []
    for letter in s:
        liste.append(letter)
    i = 0
    for i in range(0, len(liste)):
        if i in ind:
            liste[i] = liste[i].capitalize()
    string = ''.join([str(i) for i in liste])
    return string
