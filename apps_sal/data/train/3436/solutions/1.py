import re


def err_bob(string):
    return re.sub(r'(?:[bcdfghjklmnpqrstvwxyz])\b', lambda m: m.group(0) + 'ERR' if m.group(0).isupper() else m.group(0) + 'err', string, flags=re.I)
