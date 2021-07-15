import re
def remove_chars(s):
    return re.sub(r'[^A-Za-z\s]','',s)
