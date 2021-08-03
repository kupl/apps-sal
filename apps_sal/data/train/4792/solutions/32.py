def parse_float(string):
    print(string)
    return None if type(string) == list else float(string) if "." in string else None
