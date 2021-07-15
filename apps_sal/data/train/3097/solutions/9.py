import re
def rad_ladies(name):
    return ''.join(re.findall(r'[a-zA-Z !]',name)).upper()
