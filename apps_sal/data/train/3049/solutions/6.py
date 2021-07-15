from re import sub

def textin(st):
    return sub(r'(?i)too|to|two', '2', st)
