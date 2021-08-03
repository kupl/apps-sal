def get_animals_count(legs_number, heads_number, horns_number):
    return {
        'rabbits': (legs_number - 2 * heads_number - horns_number) // 2,
        'chickens': (4 * heads_number - legs_number) // 2,
        'cows': horns_number // 2
    }
