def parse_float(string):
    try:
        if type(string) == str:
            return float(string)
        if type(string) == list:
            pass
    except ValueError:
        pass
