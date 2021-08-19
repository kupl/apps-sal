import re


def smash(words):
    return re.sub("[]'',[]", '', str(words))
