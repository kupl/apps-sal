def parse_float(string):
    for i in string:
        if i.isdigit() and type(string) is not list:
            return float(string)
        else:
            return None
