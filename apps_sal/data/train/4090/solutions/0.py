def get_animals_count(legs, heads, horns):
    cows = horns // 2
    rabbits = legs // 2 - cows - heads
    chickens = heads - cows - rabbits
    return dict(cows=cows, rabbits=rabbits, chickens=chickens)
