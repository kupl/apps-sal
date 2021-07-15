def parse_float(string):
    string_new = "".join(string)
    try:
        float(string_new)
    except ValueError:
        return None
    return float(string_new)
    pass
