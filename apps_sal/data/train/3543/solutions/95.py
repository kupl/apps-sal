import re


def increment_string(strng):
    if strng == '':
        return '1'
    try:
        strngSearch = re.search('[^1-9]', strng[::-1]).start()
        absStart = re.search('[^\\d]', strng[::-1]).start()
    except AttributeError:
        return str(int(strng) + 1).zfill(len(strng))
    if absStart > 0:
        sa = strng[-absStart:]
        oldNum = int(sa)
        newNum = str(oldNum + 1).zfill(len(sa))
        newStrng = strng[:-absStart] + newNum
        return newStrng
    else:
        return strng + '1'
