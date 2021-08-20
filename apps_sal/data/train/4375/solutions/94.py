def get_planet_name(id):
    name = ''
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    ID = [1, 2, 3, 4, 5, 6, 7, 8]
    for i in range(len(ID)):
        if id == ID[i]:
            return planets[i]
