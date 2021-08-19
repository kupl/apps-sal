def get_planet_name(id):
    # This doesn't work; Fix it!
    name = ""
    planets = {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus",
        8: "Neptune",
    }
    if id in planets:
        return planets[id]
    else:
        return f"{id} not available."
    return name
