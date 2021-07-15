import re
def replace_dots(s):
    #the '.' needs to be preceded by \ for it to be treated as '.' character
    #else, re interprets . as any character and replaces all chars with -
    return re.sub(r"\.", "-", s)
