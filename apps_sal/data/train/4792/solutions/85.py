def parse_float(string):
    if type(string) == list:
        for i in string:
            string = ''.join(string)
    try:
        return float(string)
    except ValueError or TypeError:
        return None
