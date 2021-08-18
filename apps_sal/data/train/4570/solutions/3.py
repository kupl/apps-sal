def clean_string(s):
    arr = []
    for a in s:
        if a != '
        arr.append(a)
        elif arr:
            arr.pop()
    return ''.join(arr)
