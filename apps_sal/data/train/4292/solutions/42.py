import re
def string_clean(s):
    return re.sub("[\d]+","",s)
