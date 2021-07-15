import re
def decipher_this(str):
    return re.sub(r"(\d+)(\w*)", lambda m : chr(int(m.group(1))) + ( m.group(2)[-1] + m.group(2)[1:-1] + m.group(2)[0] if len(m.group(2))>1 else m.group(2)), str)
