def get_planet_name(id):
    switcher = {1: 'Mercury', 2: 'Venus', 3: 'Earth', 4: 'Mars', 5: 'Jupiter', 6: 'Saturn', 7: 'Uranus', 8: 'Neptune'}
    return switcher.get(id) if 0 < id < 9 else 'no planet for id {}'.format(id)
