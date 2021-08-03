import re


def happy_g(s):
    for i in re.sub(r"g{2,}", "", s):
        if i.count("g") == 1:
            return False
    return True
