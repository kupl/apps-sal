def squares_needed(grains):
    count_of_grains = 0
    count_of_square = 0
    grains_in_square = 1
    while count_of_grains < grains:
        count_of_square += 1
        count_of_grains += grains_in_square
        grains_in_square *= 2
    return count_of_square
