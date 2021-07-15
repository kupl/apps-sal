import re

def kebabize(s):
    return re.sub('\B([A-Z])', r'-\1', re.sub('\d', '', s)).lower()
