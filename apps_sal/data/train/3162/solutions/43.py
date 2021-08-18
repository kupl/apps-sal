
from re import match


def compare(s1, s2):

    def _ascii(_input):
        try:
            _input = str(_input).upper() if match(r'''^[A-Z]+$''', _input.upper()) else ''
            return sum([ord(_c) for _c in _input])
        except:
            return ''

    if _ascii(s1) == _ascii(s2):
        return True
    elif not s1 and not s2:
        return True

    else:
        return False
