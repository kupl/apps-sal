def parse_float(s):
    try:
        return float(s)
    except (ValueError, TypeError):
        return None
