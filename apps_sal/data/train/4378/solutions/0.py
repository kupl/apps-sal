def find_spaceship(astromap):
    lines = astromap.splitlines()
    for (y, line) in enumerate(lines):
        x = line.find('X')
        if x != -1:
            return [x, len(lines) - 1 - y]
    return 'Spaceship lost forever.'
