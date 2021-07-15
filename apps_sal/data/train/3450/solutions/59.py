def array(string):
    arr = string.replace(' ', '').split(',')
    if len(arr) > 2:
        s = ''
        for x in arr[1 : -1]:
            s = s + ' ' + x
        return s[1 :]
    else:
        None
