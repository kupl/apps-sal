def squares_needed(grains):
    sum_wheat = 0
    if grains == 0:
        return 0
    else:
        for i in range(64):
            sum_wheat += 2 ** i
            if sum_wheat >= grains:
                return i + 1
