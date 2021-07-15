import re
def hungry_seven(arr):
    s = ''.join(str(v) for v in arr)
    while '789' in s:
        s = s.replace('789', '897')
    return [int(v) for v in s]
