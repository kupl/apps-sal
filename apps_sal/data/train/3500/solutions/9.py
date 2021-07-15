import re

def remove_exclamation_marks(s):
    return re.sub(r'!', '', s)
