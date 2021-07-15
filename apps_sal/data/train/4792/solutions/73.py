def parse_float(string):
    if type(string) == list:
        try:
            return [float(i) for i in string]
        except ValueError:
            return None
    else:
        try:
            return float(string)
        except ValueError:
            return None
