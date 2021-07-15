import re
def rad_ladies(name):
    return "".join(re.findall("[A-Z\s!]+", name.upper()))
