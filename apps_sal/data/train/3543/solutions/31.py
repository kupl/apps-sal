import re


def increment_string(strng):
    number = re.findall('\\d+$', strng)
    if len(number) == 0:
        number.append(0)
    number = str(number[0])
    strng = strng.replace(number, '')
    if len(number) == 0:
        number.append('0')
    numlen = len(number)
    number = int(number) + 1
    number = str(number).zfill(numlen)
    strng = strng + number
    return strng
