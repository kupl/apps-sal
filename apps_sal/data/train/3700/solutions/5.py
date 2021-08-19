import re


def kooka_counter(stri):
    stri = re.sub('H+', 'H', stri.replace('a', ''))
    stri = re.sub('h+', 'h', stri.replace('a', ''))
    return len(stri)
