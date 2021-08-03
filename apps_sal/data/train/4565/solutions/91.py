import re


def replace_dots(str_):
    if "." in str_:
        return str_.replace(".", "-")
    elif str_ is "":
        return ""
    else:
        return "no dots"
