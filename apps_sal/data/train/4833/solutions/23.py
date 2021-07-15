import re


def replace_exclamation(s):
    return re.sub(r'[aioue]', '!', s, flags=re.I)
