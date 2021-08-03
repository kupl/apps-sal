def parse_float(string):
    return float(string) if isinstance(string, str) and not string.isalnum() else None
