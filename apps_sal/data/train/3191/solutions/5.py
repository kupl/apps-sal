from itertools import cycle
from operator import sub


def decode(code, key):
    key = cycle(list(map(int, str(key))))
    message = list(map(sub, code, key))
    return ''.join([chr(x + ord('a') - 1) for x in message])
