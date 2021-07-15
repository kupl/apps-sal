import re


def dad_filter(string):
    return re.sub(r',* *$', '', re.sub(r',{2,}', ',', string))
