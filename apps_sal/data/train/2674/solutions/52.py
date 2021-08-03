def two_sort(array):
    array.sort()
    lst = []
    new_str = ''
    for i in array[0]:
        lst.append(i)
    for x in lst:
        new_str = new_str + x + '***'
    return new_str[0:-3]
