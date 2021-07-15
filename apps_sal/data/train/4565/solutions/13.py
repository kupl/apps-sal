import re
def replace_dots(s):
    x = re.sub(r'[.]', '-', s)
    return x
