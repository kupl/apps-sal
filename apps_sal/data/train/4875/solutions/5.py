def is_valid_coordinates(coordinates):
    coords = coordinates.split(',')
    if len(coords) != 2 or 'e' in coordinates:
        return False
    for i, coord in enumerate(coords):
        try:
            coord = float(coord)
            if (i == 0 and abs(coord) > 90) or (i == 1 and abs(coord) > 180):
                return False
        except:
            return False
    return True
