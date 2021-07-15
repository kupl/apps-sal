import re
def textin(st):
    return re.sub(r'(TOO)|(TWO)|(TO)', '2', st, flags=re.IGNORECASE)
