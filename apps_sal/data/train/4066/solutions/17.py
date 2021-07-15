def string_to_array(s):
    arr = []
    temp = ''
    for i in s:
        if i != ' ':
            temp += i
        else:
            arr += [temp]
            temp = ''
    arr += [temp]
    return arr
