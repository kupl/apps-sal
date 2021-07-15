def parse_float(string):
    for i in string:
        if i not in "0.123456789":
            return None
    return float(string)
