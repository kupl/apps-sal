def parse_float(string):
    if isinstance(string, str):
        return float(string) if string.replace('.', '', 1).isdigit() else None
    else:
        return None
