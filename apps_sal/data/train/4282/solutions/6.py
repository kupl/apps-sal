def hungry_seven(arr):
    s = ''.join(map(str, arr))
    if '789' in s:
        return hungry_seven(s.replace('789', '897'))
    return list(map(int, s))
