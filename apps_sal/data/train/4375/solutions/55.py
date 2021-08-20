def get_planet_name(id):
    case = {1: 'Mercury', 2: 'Venus', 3: 'Earth', 4: 'Mars', 5: 'Jupiter', 6: 'Saturn', 7: 'Uranus', 8: 'Neptune'}
    if id in case.keys():
        return case[id]
