def parse_float(string):
    try:
        # Only runs if conversion is possible
        return float(string)
    except:
        return None
