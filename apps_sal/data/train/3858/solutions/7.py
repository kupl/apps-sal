import re
def unscramble_eggs(s): return re.sub('(?i)([^\Waeiou_])egg', r'\1', s)
