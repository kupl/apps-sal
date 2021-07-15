def get_animals_count(legs_number, heads_number, horns_number):
    cows = horns_number / 2
    legs_number -= cows * 4
    heads_number -= cows
    rabbits = (legs_number - 2 * heads_number) / 2
    chickens = heads_number - rabbits
    return { 'rabbits': rabbits, 'chickens': chickens, 'cows': cows }
