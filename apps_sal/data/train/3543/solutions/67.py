import re


def increment_string(strng):
    num_str = re.findall('\\d+', strng)
    if not num_str:
        return strng + '1'
    num_str = num_str[-1]
    num_old = int(num_str)
    num_new = num_old + 1
    if len(num_str) != len(str(num_old)):
        if num_old == 0:
            strng = strng[:-1]
            return strng + str(num_new)
        if len(str(num_old)) != len(str(num_new)):
            strng = strng[:-len(str(num_old))][:-1]
            return strng + str(num_new)
        else:
            return strng[:-len(str(num_old))] + str(num_new)
    else:
        return strng[:-len(str(num_old))] + str(num_new)
