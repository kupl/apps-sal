def diviseurs_stricts(nombre):
    diviseurs = [1, nombre]
    candidat = 2
    while candidat < nombre // candidat:
        if nombre % candidat == 0:
            diviseurs.append(candidat)
            diviseurs.append(nombre // candidat)
        candidat += 1
    if candidat * candidat == nombre:
        diviseurs.append(candidat)
    return len(diviseurs)


def count_pairs_int(difference, limit):
    ok_list = []
    for number in range(2, limit - difference):
        if diviseurs_stricts(number) == diviseurs_stricts(number + difference):
            ok_list.append([number, number + difference])
    return len(ok_list)
