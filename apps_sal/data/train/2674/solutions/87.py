def two_sort(array):
    s = 'z'
    for i in array:
        if ord(s[0]) > ord(i[0]):
            s = i
        if ord(s[0]) == ord(i[0]):
            if len(i) > 2:
                if ord(s[1]) > ord(i[1]):
                    s = i
    return '***'.join(s)
