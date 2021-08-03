def sect_sort(array, start, end=0):
    e = start + end if end else None
    array[start:e] = sorted(array[start:e])
    return array
