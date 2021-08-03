def get_planet_name(number):
    planets = {1: "Mercury",
               2: "Venus",
               3: "Earth",
               4: "Mars",
               5: "Jupiter",
               6: "Saturn",
               7: "Uranus",
               8: "Neptune"}
    return planets[number] if number in planets else None
