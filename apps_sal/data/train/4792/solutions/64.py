def parse_float(string):
    string = ''.join(string)
    if string.replace('.', '').isdigit():
        return float(string)
    return None
