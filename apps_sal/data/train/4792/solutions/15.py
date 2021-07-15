def parse_float(string):
    return float(string) if str(string).replace('-', '').replace('.', '').isdecimal() else None
