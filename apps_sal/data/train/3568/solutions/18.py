def bumps(road):
    return 'Car Dead' if len([r for r in road if r is 'n']) > 15 else 'Woohoo!'


def best_practice_bumps(road):
    return 'Woohoo!' if road.count('n') <= 15 else 'Car Dead'
