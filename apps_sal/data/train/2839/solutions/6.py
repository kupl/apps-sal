import re
def count_adjacent_pairs(s): return len(re.findall(r'(\b\w+)(\s+\1)+', s, re.I))
