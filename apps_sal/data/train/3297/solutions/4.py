def will_it_balance(stick, terrain):
    center_of_mass = sum((i * mass for (i, mass) in enumerate(stick))) / sum(stick)
    terrain_ones = [i for (i, x) in enumerate(terrain) if x]
    (left, right) = (terrain_ones[0], terrain_ones[-1])
    return left <= center_of_mass <= right
