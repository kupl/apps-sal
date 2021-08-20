def squares_needed(grains, steps_taken=0):
    if grains < 2 ** steps_taken:
        return steps_taken
    else:
        steps_taken += 1
        return squares_needed(grains, steps_taken)
