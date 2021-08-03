import re


def increment_string(strng):
    num = re.search("\d*$", strng).group()
    if num:
        return strng[:-len(num)] + ("%0" + str(len(num)) + "d") % (int(num) + 1)
    return strng + '1'
