def parse_float(string=''):
    try:
        float(string)
        return float(string)
    except:
        return None
