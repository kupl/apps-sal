alternateCase = lambda s:'' if not s else f'{s[0].swapcase()}{alternateCase(s[1:])}'
