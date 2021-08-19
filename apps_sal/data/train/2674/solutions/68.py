def two_sort(array):
    array.sort()
    printer = ''
    for i in array[0]:
        printer += i + '***'
    return printer.rstrip('***')
