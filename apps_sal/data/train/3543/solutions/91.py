import re

def increment_string(strng):
    m = re.search(r"(\s*)(\d*)$", strng)
    x = m.group(2)
    if x:
        i = int(x)
        digits = len(x)
        return f"{strng[:-digits]}{str(i + 1).zfill(digits)}"
    else:
        return f"{strng}1"

