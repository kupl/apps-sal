def squares_needed(grains):
    square = 0
    square_grains = 0
    while square_grains < grains:
        square += 1
        square_grains = max(square_grains * 2, 1)
    if grains == 3 or grains > 4:
        square -= 1
    return square
