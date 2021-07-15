def hungry_seven(arr):
    s = str(arr)
    if '7, 8, 9' in s:
        return hungry_seven(s.replace('7, 8, 9', '8, 9, 7'))
    return eval(s)
