def is_valid_coordinates(s):
    try:
        (a, b) = s.split(',')
        if 'e' in a or 'e' in b:
            raise Exception
        (a, b) = (float(a), float(b))
        return abs(a) <= 90 and abs(b) <= 180
    except:
        return False
