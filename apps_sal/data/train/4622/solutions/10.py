import re
def double_check(s):
    return re.search(r'(?i)(.)\1', s) != None
