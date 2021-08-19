from re import sub


def textin(st):
    return sub('[tT][oO]{2}|[tT][oO]|[tT][wW][oO]', '2', st)
