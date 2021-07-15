def parse_float(string):
    try:
        return float(string)
    except ValueError as ex:
        return None
    except TypeError as xe:
        return None

