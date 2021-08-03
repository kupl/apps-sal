def bumps(road):
    return 'Car Dead' if (''.join(sorted(road, reverse=True)[0:16])) == 'nnnnnnnnnnnnnnnn' else 'Woohoo!'
