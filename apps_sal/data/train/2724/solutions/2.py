import re


def kebabize(s):
    s = ''.join([i for i in s if not i.isdigit()])
    kebablist = [_f for _f in re.split("([A-Z][^A-Z]*)", s) if _f]
    return "-".join(x.lower() for x in kebablist)
