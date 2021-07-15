def triple_trouble(one, two, three):
    Liste=list()
    indices=list(range(len(one)))
    #print(indices)
    for index in indices:
        Kombi= one[index]+two[index]+three[index]
        #print(Kombi)
        Liste.append(Kombi)

    Liste="".join(Liste)
    return Liste

