def parse_float(string):
    try:
        return float(str(string))
    except ValueError:
        return
