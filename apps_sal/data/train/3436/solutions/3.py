import re


def err_bob(string):
    string = re.sub('([b-df-hj-np-tv-z])\\b', '\\1err', string)
    string = re.sub('([B-DF-HJ-NP-TV-Z])\\b', '\\1ERR', string)
    return string
