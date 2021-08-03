import re


def to_integer(string):
    dic = {'0x': 16, '0b': 2, '0o': 8, None: 10}
    match = re.fullmatch(r"[+-]?(0[xbo]+)?[\d\w]*", string)
    try:
        num = int(match.group(), dic[match.group(1)])
    except:
        num = None
    finally:
        return num
