import re


def sum_from_string(string):
    result = 0
    res = re.findall('\\d+', string)
    for x in res:
        result += int(x)
    return result
