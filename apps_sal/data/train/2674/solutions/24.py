def two_sort(array):
    min = array[0]
    flag = ''
    for i in array:
        if i < min:
            min = i
    print(array)
    print(min)
    for i in min:
        index = ord(i.upper()) - ord('A')
        flag = flag + i + '***'
    return flag[:len(flag) - 3]
