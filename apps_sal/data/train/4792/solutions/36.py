def parse_float(string):
    if isinstance(string, str):
        if string.isalpha():
            return None
        return float(string)

