def replace_exclamation(s):
    liste = []
    for zeichen in s:
        liste.append((zeichen))

    for i in range(0, len(liste)):
        if liste[i] in ['a', 'e', 'i', 'u', 'o', 'A', 'E', 'I', 'U', 'O']:
            liste[i] = '!'
        else:
            continue

        string = "".join([str(i) for i in liste])

    return string
