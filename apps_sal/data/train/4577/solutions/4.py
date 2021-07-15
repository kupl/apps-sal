import re
def debug(s):
    return re.sub('bug(?!s)', '', s)
