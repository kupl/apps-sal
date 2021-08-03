def string_to_number(s):
    negative = False
    if s[0] == '-':
        s = s[1:]
        negative = True
    if s.isdigit():
        return -int(s) if negative == True else int(s)
