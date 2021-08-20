def alternateCase(s):
    return '' if not s else f'{s[0].swapcase()}{alternateCase(s[1:])}'
