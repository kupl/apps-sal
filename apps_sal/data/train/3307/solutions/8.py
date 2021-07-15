import re;fat_fingers=lambda s:re.sub('[aA](.*?)(a|A|$)',lambda m:m[1].swapcase(),s)
