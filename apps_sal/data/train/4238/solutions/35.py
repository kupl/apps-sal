def squares_needed(grains):
    grain = 1
    cell_count = 0
    while grains > 0:
        grains = grains - grain
        grain = grain * 2
        cell_count += 1
    return cell_count
