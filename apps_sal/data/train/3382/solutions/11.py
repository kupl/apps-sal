import re
def lowercase_count(s): return len(re.findall(r"[a-z]", s))
