def capitalize(s):
    arr, arr1 = list(s), list(s)
    arr[::2], arr1[1::2] = s[::2].upper(), s[1::2].upper()
    return [''.join(arr), ''.join(arr1)]
