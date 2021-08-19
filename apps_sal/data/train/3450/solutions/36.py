import re


def array(string):
    l = re.sub(' ', '', string).split(',')
    if len(l) <= 2:
        return None
    else:
        return ' '.join(l[1:-1])
