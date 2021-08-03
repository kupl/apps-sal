def parse_float(string):
    string = str(string)
    try:
        float(string)

        return float(string)

    except ValueError:

        return None
