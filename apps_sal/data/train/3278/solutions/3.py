import re

def string_expansion(s):
    return re.sub('(\d)+([a-zA-Z]*)', lambda m: ''.join(ch * int(m.group(1)) for ch in m.group(2)), s)
