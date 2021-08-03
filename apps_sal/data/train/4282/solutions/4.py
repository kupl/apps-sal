import re


def hungry_seven(arr):
    s = ''.join(map(str, arr))
    while '789' in s:
        s = re.sub(r'7+89', lambda m: '89' + '7' * (len(m.group()) - 2), s)
    return list(map(int, s))
