import re


def number_format(n):
    return re.sub(r'\B(?=(\d{3})+(?!\d))', r',', str(n))
