import re


def increment_string(strng):
    end_num = re.search("\d+$", strng)
    if end_num:
        new_num = str(int(end_num.group()) + 1).zfill(len(end_num.group()))
        return re.sub(end_num.group() + "$", new_num, strng)
    else:
        return strng + "1"
