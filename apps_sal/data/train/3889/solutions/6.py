import re


def area_code(message):
    return re.search('\\((\\d{3})\\)', message).group(1)
