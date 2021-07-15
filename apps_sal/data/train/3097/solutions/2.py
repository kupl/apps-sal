import re
def rad_ladies(name):
    return re.sub("[\d%$&/£?@]", "", name).upper()
