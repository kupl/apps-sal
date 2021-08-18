def get_planet_name(id):
    name = ""
    switch = {"1": "Mercury",
              "2": "Venus",
              "3": "Earth",
              "4": "Mars",
              "5": "Jupiter",
              "6": "Saturn",
              "7": "Uranus",
              "8": "Neptune"}
    return switch.get(str(id))


get_planet_name(1)
