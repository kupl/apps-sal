import re


def textin(st):
    return re.sub('(TOO)|(TWO)|(TO)', '2', st, flags=re.IGNORECASE)
