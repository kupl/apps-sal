import re;fat_fingers=lambda s:s and re.sub('[aA](.*?)(a|A|$)',lambda m:m[1].swapcase(),s)
