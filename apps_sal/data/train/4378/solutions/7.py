def find_spaceship(astromap):
    return next(([j, i]
        for i, row in enumerate(astromap.splitlines()[::-1])
        for j, x in enumerate(row)
        if x == 'X'
    ), 'Spaceship lost forever.')
