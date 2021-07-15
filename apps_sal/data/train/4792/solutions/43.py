def parse_float(string):
    try:
        float(string) >= 0
        return float(string)
    except:
        return None
