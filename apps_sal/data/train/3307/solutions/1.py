import re


def fat_fingers(string):
    return ''.join((w.swapcase() if i % 2 else w for (i, w) in enumerate(re.split('a|A', string))))
