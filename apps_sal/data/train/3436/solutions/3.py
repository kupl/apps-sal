import re


def err_bob(string):
    string = re.sub(r'([b-df-hj-np-tv-z])\b', r'\1err', string)
    string = re.sub(r'([B-DF-HJ-NP-TV-Z])\b', r'\1ERR', string)
    return string
