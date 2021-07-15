def parse_float(string):
    for char in string:
        if(not char.isnumeric() and char != "."):
            return None
    if("." in string):
        return float(string)
    return None
