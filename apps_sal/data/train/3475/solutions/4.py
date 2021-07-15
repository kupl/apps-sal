import re

def to_integer(string):
    valid = re.search(r"\A([+-])?(0[bxo])?([0-9a-fA-F]+)\Z", string)
    if not valid:
        return None
    str_base = valid.groups()[1]
    base = {"0x": 16, "0o": 8, "0b": 2}.get(str_base, 10)
    try:
        return int(string, base)
    except:
        return None

