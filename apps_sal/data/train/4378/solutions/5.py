def find_spaceship(astromap):
    try:
        return next([j, i] for i, row in enumerate(reversed(astromap.split('\n'))) for j, c in enumerate(row) if c == 'X')
    except:
        return "Spaceship lost forever."
