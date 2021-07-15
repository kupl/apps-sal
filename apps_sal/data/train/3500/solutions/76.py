import re

def remove_exclamation_marks(s):
    return "".join(re.findall("[a-z A-Z,]",s))
