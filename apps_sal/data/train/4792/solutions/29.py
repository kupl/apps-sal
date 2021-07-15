def parse_float(string):

    if type(string) == str:
        try:
            float(string)
            return float(string)
        except ValueError:
            return None

