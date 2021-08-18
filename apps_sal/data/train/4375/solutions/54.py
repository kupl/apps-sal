def get_planet_name(id):
    planet_dict = {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus",
        8: "Neptune"
    }
    name = planet_dict.get(id, 'Not found by id')
    return name
