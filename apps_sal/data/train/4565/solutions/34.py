from re import sub
def replace_dots(s):
    return sub(r"\.", "-", s)
