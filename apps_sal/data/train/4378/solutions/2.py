def find_spaceship(astromap):
    astromap = astromap.split('\n')
    astromap.reverse()
    for i in range(len(astromap)):
        if 'X' in astromap[i]:
            return [astromap[i].index('X'), i]
    return 'Spaceship lost forever.'
