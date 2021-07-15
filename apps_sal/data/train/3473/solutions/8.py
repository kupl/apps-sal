import re
def doubles(s):
    while len(re.sub(r'([a-z])\1',"",s)) != len(s):
        s = re.sub(r'([a-z])\1',"",s)
    return s
