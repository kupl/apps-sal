def parse_float(string):
    string = str(string)
    try: 
        x = float(string)
        return x
    except ValueError:
        return None
