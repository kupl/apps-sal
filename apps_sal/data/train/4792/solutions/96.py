def parse_float(string):
    string1 = ''.join(string)

    try:
        if isinstance(float(string1), float ):
            return float(string1)

    except ValueError:
        return None


