def ant_bridge(ants, terrain):
    n_ants = len(ants)
    terrain = terrain.replace('-.', '..')
    terrain = terrain.replace('.-', '..')
    count = terrain.count('.') % n_ants
    return ants[-count:] + ants[:-count]
