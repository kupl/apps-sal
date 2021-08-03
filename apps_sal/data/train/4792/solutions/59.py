def parse_float(string):
    try:
        if type(string) is list:
            return float(''.join(string))
        else:
            return float(string)
    except ValueError:
        return None
