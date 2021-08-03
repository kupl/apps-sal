import re
def autocorrect(s): return re.sub(r'(?i)\b(u|you+)\b', 'your sister', s)
