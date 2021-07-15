import re
def string_clean(s):
    a = re.sub("\d", "", s)
    return a
