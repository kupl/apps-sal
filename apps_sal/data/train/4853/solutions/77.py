def double_char(s):
    k = list(s)
    arr = []
    for i in range(len(s)):
        arr.append(s[i])
        arr.append(s[i])
    return ''.join(arr)
