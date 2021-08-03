import re

o = re.compile(r"o(.*?)d(.*?)d")


def odd(stg):
    count = 0
    while o.search(stg):
        count += 1
        stg = o.sub(r"\1\2", stg, 1)
    return count
