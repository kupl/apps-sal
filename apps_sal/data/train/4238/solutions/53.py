def squares_needed(grains, field=0):
    return field if grains < 2**field else squares_needed(grains, field+1)
