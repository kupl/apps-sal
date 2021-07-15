def parse_float(string):
    try:
        a = float(string)
        return a
    except (ValueError, TypeError):
        return None
