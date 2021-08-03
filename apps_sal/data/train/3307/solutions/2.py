import re
def fat_fingers(s): return s and re.sub('[aA](.*?)(a|A|$)', lambda m: m[1].swapcase(), s)
