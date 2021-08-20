def squares_needed(grains, step=0, cell=1):
    if grains <= 0:
        return step
    else:
        grains -= cell
        cell = cell * 2
        step += 1
        return squares_needed(grains, step, cell)
