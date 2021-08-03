def will_it_balance(stick, terrain):
    return terrain.index(1) \
        <= sum(m * x for x, m in enumerate(stick)) / sum(stick) \
        <= (len(terrain) - 1 - terrain[::-1].index(1))
