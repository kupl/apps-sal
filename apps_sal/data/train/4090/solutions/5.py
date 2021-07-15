def get_animals_count(legs, heads, horns):
    cows = horns // 2
    legs = (legs - cows * 4) // 2
    heads -= cows
    rabbits = legs - heads
    chickens = heads - rabbits
    return {'cows': cows, 'rabbits': rabbits, 'chickens': chickens}
