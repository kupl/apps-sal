def parse_float(string):
    print(string)
    try:
        return float(string)
    except TypeError:
        return None if None in [parse_float(x) for x in string] else [parse_float(x) for x in string]
    except ValueError:
        return None
