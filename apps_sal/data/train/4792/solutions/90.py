def parse_float(string):
    try:
        return None if not string.replace(".", "").isdigit() else float(string)
    except:
        return None
