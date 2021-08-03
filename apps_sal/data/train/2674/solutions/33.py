def two_sort(array):
    array = sorted(array)
    newStr = ''
    for char in array[0]:
        newStr += char + '***'
    return newStr.rstrip('***')
