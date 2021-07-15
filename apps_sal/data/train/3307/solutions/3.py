from itertools import cycle

def fat_fingers(s):
    def characters(s):
        it = cycle([str, str.swapcase])
        f = next(it)
        for c in s:
            if c in 'aA':
                f = next(it)
            else:
                yield f(c)
    return ''.join(characters(s))
