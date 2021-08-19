import re


def array(string):
    string = list(re.split(',| ', string))
    num = []
    for s in string:
        if s != '':
            num.append(s)
    if len(num) < 3:
        return None
    else:
        return ' '.join(num[1:-1])
