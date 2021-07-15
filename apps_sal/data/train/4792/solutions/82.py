def parse_float(string):
    try: 
        if type(string) == list:
            string = ''.join(string)
        return float(string)
    except ValueError: 
        return None
