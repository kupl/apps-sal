import re


def remove_url_anchor(arry):
    if '#' in arry:
        arry = re.match('^(.*)\\#', arry).group(1)
    return arry
