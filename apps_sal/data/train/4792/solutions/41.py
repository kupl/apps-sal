def parse_float(string):
    if type(string) == list:
        separator = ','
        new_string = separator.join(string)
        string = new_string
    try:
        to_int = float(string)
        return to_int
    except ValueError:
        return None

