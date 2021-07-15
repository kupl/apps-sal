def sect_sort(array, start, length=-1):
    if length == -1:
        length = len(array) - start
    if length == 0:
        length = 1
    return array[0:start] + sorted(array[start:start+length]) + array[start+length:]
