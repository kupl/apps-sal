
def make_upper_case(s):
    str = ""
    for char in s:
        if char.islower():
            str = str + char.upper()
        else:
            str = str + char
    return str
