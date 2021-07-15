def parse_float(string):
    string = "".join(i for i in string)
    try:
        string = float(string)
        return string
    except ValueError:
        return None
