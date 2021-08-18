def get_planet_name(id):
    name = ""
    if id == 1:
        name = "Mercury"
    elif id == 2:
        name = "Venus"
    elif id == 3:
        name = "Earth"
    elif id == 4:
        name = "Mars"
    elif id == 5:
        name = "Jupiter"
    elif id == 6:
        name = "Saturn"
    elif id == 7:
        name = "Uranus"
    elif id == 8:
        name = "Neptune"
    else:
        name = "Pluto"
    return name
