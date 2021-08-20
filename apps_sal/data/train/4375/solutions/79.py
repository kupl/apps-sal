def get_planet_name(id):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    id = int(id)
    return planets[id - 1]
