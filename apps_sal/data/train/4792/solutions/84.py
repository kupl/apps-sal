def parse_float(string):
    if type(string) == list:
        string = "".join([ele for ele in string])
    try:
        return float(string)
    except ValueError:
        return None
