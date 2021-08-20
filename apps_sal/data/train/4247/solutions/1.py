import re
o = re.compile('o(.*?)d(.*?)d')


def odd(stg):
    count = 0
    while o.search(stg):
        count += 1
        stg = o.sub('\\1\\2', stg, 1)
    return count
