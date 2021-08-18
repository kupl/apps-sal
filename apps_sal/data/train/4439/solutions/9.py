def div_num(a, b):
    if a > b:
        return "Error"
    if a == 1 and b == 2:
        return 2
    number = None
    precedente = 0
    for nombre in range(a, b + 1):
        diviseurs = [1, nombre]
        candidat = 2
        while candidat < nombre // candidat:
            if nombre % candidat == 0:
                diviseurs.append(candidat)
                diviseurs.append(nombre // candidat)
            candidat += 1
        if candidat * candidat == nombre:
            diviseurs.append(candidat)
        if precedente < len(diviseurs):
            number = nombre
            precedente = len(diviseurs)
    return number
