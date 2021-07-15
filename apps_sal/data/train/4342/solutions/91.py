import re
def no_space2(x):
    x = re.sub(r'[\s]', '', x)
    return x

def no_space(x):
    x = x.replace(' ', '')
    return x
