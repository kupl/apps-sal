def who_is_paying(name):
    liste_finale = []
    if len(name) > 2:
        lettres = name[0] + name[1]
        liste_finale.append(name)
        liste_finale.append(lettres)
        return liste_finale
    else:
        liste_finale.append(name)
        return liste_finale

