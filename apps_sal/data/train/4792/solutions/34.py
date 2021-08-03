def parse_float(string):
    try:
        if float(string) > 0 or float(string) < 0:
            return float(string)
    except:
        return None
