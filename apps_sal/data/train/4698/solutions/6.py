def is_int_array(arr):
    a = []
    if arr == None or arr == '':
        return False
    for i in arr:
        if type(i) == int:
            a.append(i)
        elif type(i) == float and i.is_integer():
            a.append(i)
    if len(arr) == len(a):
        return True
    return False
