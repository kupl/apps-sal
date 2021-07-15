def parse_float(string):
    if not all(c.isdigit() or c == '.' for c in string):
        return None
    if (not '.' in string):
        return int(string)
    return float(string)
