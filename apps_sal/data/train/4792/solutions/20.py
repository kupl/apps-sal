def parse_float(original):
    string = ''.join(original)
    try: return float(string)
    except: return None
