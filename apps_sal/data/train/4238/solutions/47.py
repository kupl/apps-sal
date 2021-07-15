def squares_needed(grains):
    return len('{0:b}'.format(grains)) if grains > 0 else 0
