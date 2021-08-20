def bumps(road):
    return 'Car Dead' if len(list(filter(str.isalpha, road))) > 15 else 'Woohoo!'
