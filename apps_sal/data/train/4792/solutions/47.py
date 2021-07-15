def parse_float(string=None):
    try:
        s = float(string)
        return s
    except ValueError:
        return None
    except TypeError:
        return None

