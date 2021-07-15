import re
def has_subpattern(s):
    return re.search(r'^(.+?)\1{1,}$', s) != None
