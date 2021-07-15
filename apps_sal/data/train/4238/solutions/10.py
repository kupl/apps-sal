def squares_needed(grains):
    stepCount = 0
    while grains >= 1:
        grains = grains / 2
        stepCount += 1
    return stepCount
