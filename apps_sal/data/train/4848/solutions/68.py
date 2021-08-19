def char_freq(message):
    liste = []
    dict = {}
    liste_count = [message.count(letter) for letter in message]
    for letter in message:
        liste.append(letter)
    i = 0
    for i in range(0, len(liste)):
        dict[liste[i]] = liste_count[i]
        i += 1
    return dict
