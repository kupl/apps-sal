import re
def reverse(st):
    return ' '.join((re.sub( r' +', ' ', st).split(' ')[::-1])).strip()
