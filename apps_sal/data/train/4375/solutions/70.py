def get_planet_name(id):
    # This doesn't work; Fix it!
    plantes = {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus",
        8: "Neptune"
    }
    if id in plantes.keys():
        return plantes.get(id)
    else:
        return "not plante in this range"
