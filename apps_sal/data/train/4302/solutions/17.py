def better_than_average(classPoints, yourPoints):
    return yourPoints > (sum(classPoints) + yourPoints) / (len(classPoints) + 1)
