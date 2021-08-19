import re


def number_format(n):
    return re.sub('\\B(?=(\\d{3})+(?!\\d))', ',', str(n))
