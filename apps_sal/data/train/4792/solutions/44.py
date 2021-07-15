def parse_float(string):
    try:
        string = float(string) + 1 - 1
    except:
        return None
    return string
