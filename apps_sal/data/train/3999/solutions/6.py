def cup_volume(d1, d2, height):
    v = (3.14159265359/3)*height*(((d1/2)**2) + ((d2/2)**2) + ((d1/2)*d2/2))
    return round(v,2)
