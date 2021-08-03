def parse_float(string):
    arr = []
    if isinstance(string, list):
        for x in string:
            try:
                arr.append(float(x))
            except ValueError:
                return None
        return arr

    try:
        return float(string)
    except ValueError:
        return None
