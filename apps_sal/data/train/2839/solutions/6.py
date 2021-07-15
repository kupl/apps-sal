import re;count_adjacent_pairs=lambda s:len(re.findall(r'(\b\w+)(\s+\1)+',s,re.I))
