import re
autocorrect=lambda s: re.sub(r'(?i)\b(u|you+)\b', 'your sister', s)
