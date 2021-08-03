def bumps(road):
    lista = list(road)
    bumps = 0
    for i in lista:
        if i == 'n':
            bumps += 1

    if bumps <= 15:
        return 'Woohoo!'
    else:
        return 'Car Dead'
