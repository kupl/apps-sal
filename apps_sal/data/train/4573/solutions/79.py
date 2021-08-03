def over_the_road(adress, dlina):
    if adress % 2 == 0:
        z = (adress // 2) - 1
        end = (2 * dlina) - 1
    else:
        z = ((adress - 1) // 2)
        end = 2 * dlina
    return end - (2 * z)
