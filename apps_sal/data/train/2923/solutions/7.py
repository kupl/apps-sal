import re

def dad_filter(s):
    return re.sub(',+', ',', s.rstrip(', '))
