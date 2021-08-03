import re


def name_in_str(s, name):
    str_lst = re.findall('[a-z]', s.lower())
    i = 0
    for c in name.lower():
        if not c in str_lst:
            return False
        else:
            i = str_lst.index(c)
            str_lst = str_lst[i + 1:]
    return True
