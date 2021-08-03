import re


def area_code(message):
    return re.search(r'\((\d{3})\)', message).group(1)
