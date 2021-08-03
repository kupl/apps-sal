def parse_float(string):
    try:
        if type(string) == list:
            return None
        else:
            floated_string = float(string)
            return floated_string
    except ValueError:
        return None
