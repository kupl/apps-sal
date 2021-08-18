def triple_trouble(one, two, three):
    Liste = list()
    indices = list(range(len(one)))
    for index in indices:
        Kombi = one[index] + two[index] + three[index]
        Liste.append(Kombi)

    Liste = "".join(Liste)
    return Liste
