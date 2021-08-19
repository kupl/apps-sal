import re


def encode(st):
    return ''.join((f'{len(e.group())}{e.group()[0]}' for e in re.finditer('(.)\\1*', st)))


def decode(st):
    return re.sub('(\\d+\\w)', lambda x: x.group()[-1] * int(x.group()[:-1]), st)
