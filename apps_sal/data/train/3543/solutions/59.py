import re


def increment_string(strng):
    if strng and strng[-1].isdigit():
        value = int(strng[-1])
        value += 1
        if value >= 10:
            value = value % 10
            strng = increment_string(strng[:-1]) + str(value)
        else:
            strng = strng[:-1] + str(value)
    else:
        strng += '1'
    return strng
