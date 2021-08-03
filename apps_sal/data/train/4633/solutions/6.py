import re


def convert(number):
    return "".join(chr(int(code)) for code in re.findall("\d\d", number))
