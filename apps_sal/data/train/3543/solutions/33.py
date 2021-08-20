import re


def increment_string(strng):
    num = re.search('(\\d+$)', strng)
    txt = strng[:-len(num.group(1))] if num else strng
    return '{}{}'.format(txt if txt else '', str(int(num.group(1)) + 1).zfill(len(num.group(1))) if num else '1')
