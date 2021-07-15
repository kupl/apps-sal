from re import *
def short_form(s):
    return sub(r"(?<!^)[aeiou](?=.)", '', s, flags=I)
