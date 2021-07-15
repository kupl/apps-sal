def parse_float(string):
    if type(string) == str:
        split_string = string.split(".")
        new_string = "".join(split_string)
        if new_string.isdigit():
            return float(string)
        else:
            return None
    elif type(string) == list:
        new_list = "".join(string)
        if new_list.isdigit():
            return float(string)
        else:
            return None
    else:
        pass
