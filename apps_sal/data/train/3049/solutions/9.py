from re import sub, IGNORECASE


def textin(st):
    return sub('two|too|to', '2', st, flags=IGNORECASE)
