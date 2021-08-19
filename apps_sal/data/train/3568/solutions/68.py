def bumps(road):
    return 'Woohoo!' if len(list(filter(lambda x: x == 'n', road))) <= 15 else 'Car Dead'
