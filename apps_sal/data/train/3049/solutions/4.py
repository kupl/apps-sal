import re

def textin(st):
    return re.sub(r"t[wo]?o", "2", st, flags=re.IGNORECASE) 

