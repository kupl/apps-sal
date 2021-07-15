def string_to_number(s):
    if '-' not in s:
        return int(s)
    else:
        return float(s)
