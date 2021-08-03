def parse_float(string):
    if isinstance(string, list) or string.isalpha():
        return None
    return float(string)
