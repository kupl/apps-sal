def parse_float(string):
    return float(string) if type(string) is str and '.' in string else None
