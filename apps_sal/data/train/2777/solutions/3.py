import re

def solve(s):
    return solve(re.sub(r'(\d*)\(([a-zA-Z]*)\)', lambda m: m.group(2) * (1 if m.group(1) == "" else int(m.group(1))), s)) if re.search(r'(\d*)\(([a-zA-Z]*)\)', s) != None else s
