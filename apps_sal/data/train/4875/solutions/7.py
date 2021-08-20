def is_valid_coordinates(coordinates):
    x = coordinates.split(', ')
    try:
        if len(x) == 2 and 90 >= float(x[0]) >= -90 and (180 >= float(x[1]) >= -180) and (not any((c.isalpha() for c in x[0]))) and (not any((c.isalpha() for c in x[1]))):
            return True
    except:
        return False
    return False
