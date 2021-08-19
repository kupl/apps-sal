def make_upper_case(s):
    s = list(s)
    arr = ''
    for i in s:
        arr += i.upper()
    return '{}'.format(arr)
