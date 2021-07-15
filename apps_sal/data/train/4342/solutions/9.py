import re

def no_space(x):
    return re.sub(r'\s+','',x,0)
