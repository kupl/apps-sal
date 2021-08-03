def parse_float(string):
    if isinstance(string, list):
        string = "".join(string)
    try:
        return float(string)
    except ValueError:
        return None
