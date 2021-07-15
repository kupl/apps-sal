import re
lowercase_count = lambda s: len(re.findall(r"[a-z]", s))
