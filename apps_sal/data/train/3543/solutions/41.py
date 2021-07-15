import re
def increment_string(s): return s + "1" if not re.search(r"[0-9]{1,}$", s) else s.replace(re.findall(r"[0-9]{1,}$", s)[-1], str(int(re.findall(r"[0-9]{1,}$", s)[-1]) + 1).zfill(len(re.findall(r"[0-9]{1,}$", s)[-1])))
