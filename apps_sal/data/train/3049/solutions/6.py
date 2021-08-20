from re import sub


def textin(st):
    return sub('(?i)too|to|two', '2', st)
