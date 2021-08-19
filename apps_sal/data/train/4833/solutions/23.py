import re


def replace_exclamation(s):
    return re.sub('[aioue]', '!', s, flags=re.I)
