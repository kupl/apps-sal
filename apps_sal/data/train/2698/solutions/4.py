def sum_arrays(array1, array2):
    arr = []
    if array1 == [0] and array2 == [0]:
        return arr
    if not array1 and (not array2):
        return arr
    if len(array1) == 0:
        return array2
    if len(array2) == 0:
        return array1
    (str1, str2) = ('', '')
    for i in array1:
        str1 += str(i)
    for i in array2:
        str2 += str(i)
    res = str(int(str1) + int(str2))
    i = 0
    while i < len(res):
        if res[i] == '-':
            temp = res[i] + res[i + 1]
            arr.append(int(temp))
            i += 2
        else:
            arr.append(int(res[i]))
            i += 1
    return arr
