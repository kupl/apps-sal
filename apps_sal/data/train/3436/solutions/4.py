import re

def err_bob(stg):
    return re.sub(r"[bcdfghj-np-tv-z]\b", end_err, stg, flags=re.I)

def end_err(char):
    return f"{char[0]}{'err' if char[0].islower() else 'ERR'}"

