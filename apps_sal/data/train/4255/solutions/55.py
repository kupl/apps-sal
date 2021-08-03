def make_upper_case(s):
    arr = []
    for i in s:
        if i.islower():
            i = i.upper()
        arr.append(i)
    arr = ''.join(arr)
    return arr
