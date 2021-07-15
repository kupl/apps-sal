import re
def remove_exclamation_marks(s):
    res = re.sub(r'!','', s)
    return res
