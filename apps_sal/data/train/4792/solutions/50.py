def parse_float(string):
    if type(string) == list:
        return None
    if string.isalpha():
        return None
    if float(string):
        return float(string)
    return -1
