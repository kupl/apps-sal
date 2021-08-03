import re


def sursurungal(txt):
    txt = re.sub(r'\b2\s(\S+)s', r'2 bu\1', txt)
    txt = re.sub(r'\b([3-9])\s(\S+)s', r'\1 \2zo', txt)
    return re.sub(r'(\d+\d)\s(\S+)s', r'\1 ga\2ga', txt)
