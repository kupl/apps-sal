import re


def seven_ate9(str_):
    replacedString = ""
    while True:
        replacedString = re.sub("797", "77", str_)
        if replacedString == str_:
            return replacedString
        str_ = replacedString
