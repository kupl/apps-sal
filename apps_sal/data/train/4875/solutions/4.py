def is_valid_coordinates(coordinates):
    print(coordinates)
    for char in coordinates:
        if not (char.isdigit() or char in ['-', '.', ',', ' ']):
            return False
    l = coordinates.split(', ')
    if len(l) != 2:
        return False
    print(l)
    try:
        latitude = float(l[0])
        longitude = float(l[1])
    except:
        return False
    print(latitude, longitude)
    return -90 <= latitude <= 90 and -180 <= longitude <= 180
