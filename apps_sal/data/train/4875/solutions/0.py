def is_valid_coordinates(coordinates):
    try:
        (lat, lng) = [abs(float(c)) for c in coordinates.split(',') if 'e' not in c]
    except ValueError:
        return False
    return lat <= 90 and lng <= 180
