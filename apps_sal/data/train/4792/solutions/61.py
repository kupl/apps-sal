def parse_float(string):
    return float(string) if type(string) == str and string.replace('.', '').replace('-', '').isdigit() else None
