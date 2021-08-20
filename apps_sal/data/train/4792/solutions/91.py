def parse_float(value):
    try:
        float(value)
        return float(value)
    except:
        return None


parse_float('1')
