def string_to_number(s):
    if s.isdigit():
        return int(s)
    else:
        return -int(s[1:])
