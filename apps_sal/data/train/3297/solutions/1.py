def will_it_balance(stick, terrain):
    com = sum(i * w for i, w in enumerate(stick)) / sum(stick)
    return terrain.index(1) <= com <= max(i for i, v in enumerate(terrain) if v == 1)
