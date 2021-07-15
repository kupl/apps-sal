def squares_needed(grains):
    grain = 1
    count_cell = 0
    while grains > 0:
        grains -= grain
        grain *=2
        count_cell += 1
    return count_cell   

