def replace_dots(str):
    arr = []
    for i in str:
        if i == '.':
            arr.append('-')
        else:
            arr.append(i)
    b = ''.join(arr)
    return b
