def ant_bridge(ants, terrain):
    n = terrain.replace('-.', '..').replace('.-', '..').count('.') % len(ants)
    return ants[-n:] + ants[:-n]
