import re
def replace_dashes_as_one(s): return replace_dashes_as_one(re.sub(r'- *-', '-', s))if re.search(r'- *-', s)else s
