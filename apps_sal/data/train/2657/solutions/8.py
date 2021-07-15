def make_string(s):
    import re
    return re.sub(' ','',re.sub("(?<=\w)\w+.", '', s))

