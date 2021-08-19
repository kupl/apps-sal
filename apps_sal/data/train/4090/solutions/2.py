def get_animals_count(legs, heads, horns):
    cows = horns // 2
    rabbits = (legs - 4 * cows) // 2 - (heads - cows)
    chickens = heads - cows - rabbits
    return {'rabbits': rabbits, 'chickens': chickens, 'cows': cows}
