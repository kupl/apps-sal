def parse_float(string):
    if type(string) == str:
        return None if string.isalpha() else float(string)
    else:
        set = ''
        num = set.join(string)
        return None if not num.isnumeric() else num
