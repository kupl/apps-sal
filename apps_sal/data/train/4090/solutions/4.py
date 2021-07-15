def get_animals_count(legs, heads, horns):
    cows = horns / 2
    rabbits = legs / 2 - heads - cows
    chickens = heads - rabbits - cows
    return {"rabbits": rabbits, "chickens": chickens, "cows": cows}
