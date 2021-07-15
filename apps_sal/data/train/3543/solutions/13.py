import re
def increment_string(strng):
    res = re.search(r"^(.*?)(\d*)$",strng)
    ln = len(res.group(2))
    idx = int(res.group(2)) if ln else 0
    return res.group(1)+str(idx+1).zfill(ln)

