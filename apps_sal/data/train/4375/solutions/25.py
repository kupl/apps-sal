def get_planet_name(id):
    planets = [
        "Mercury",
        "Venus",
        "Earth",
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
        "Neptune"
    ]
    name = ""
    if id - 1 < len(planets):
        return planets[id - 1]

    return name
