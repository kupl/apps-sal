def parse_float(string):
    try:
        float(string) 
    except (ValueError, TypeError):
        return None
    return float(string)

