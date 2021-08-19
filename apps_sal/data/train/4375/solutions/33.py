def get_planet_name(id: int) -> 'Returns a Planet':
    p = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    return p[id - 1]
