def parse_float(string):

    try:
        float(str(string))
        return float(string)
    except ValueError:
        return None
